# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_18:15:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,434 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 18:15:56 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:14:21 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:07:54 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-04-29 18:07:42 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:06:45 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:06:35 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.058 |  |
| 2026-04-29 18:05:48 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:05:10 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.067 |  |
| 2026-04-29 18:04:54 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 18:04:34 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 18:04:34 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:04:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:03:44 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:03:42 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-04-29 18:03:10 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 18:03:07 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-29 18:02:58 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-04-29 18:02:31 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:02:22 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:02:19 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:02:13 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.022 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-29 18:01:52 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-04-29 18:01:48 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:01:48 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:01:41 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-29 18:01:26 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-29 18:01:24 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:01:21 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:01:08 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:00:57 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 18:00:51 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:00:40 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-29 18:00:37 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.099 |  |
| 2026-04-29 18:00:32 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.050 |  |
| 2026-04-29 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-29 17:54:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.012 |  |
| 2026-04-29 17:38:36 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 18:07:54 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-04-29 18:01:52 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-04-29 18:01:26 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-29 18:01:41 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-29 18:00:40 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-29 18:04:54 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 18:00:57 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 18:04:34 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 18:01:48 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:06:45 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:07:42 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:01:48 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:04:34 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:14:21 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:01:08 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:02:22 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:04:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:01:21 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:15:56 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 18:03:10 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:02:31 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:01:24 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:00:51 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:05:48 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-29 18:02:19 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-29 17:01:45 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-04-29 17:54:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.012 |  |
| 2026-04-29 18:03:42 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-04-29 18:02:58 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-04-29 18:02:13 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.022 |  |
| 2026-04-29 18:03:07 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-29 18:00:32 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.050 |  |
| 2026-04-29 18:06:35 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.058 |  |
| 2026-04-29 18:05:10 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.067 |  |
| 2026-04-29 18:00:37 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)