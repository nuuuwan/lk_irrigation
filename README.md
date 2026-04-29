# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_22:15:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,577 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 22:15:10 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.037 |  |
| 2026-04-29 22:13:08 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.046 |  |
| 2026-04-29 22:11:47 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:09:32 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 22:09:23 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.036 |  |
| 2026-04-29 22:09:21 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-29 22:08:48 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-04-29 22:08:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:06:15 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:06:05 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-29 22:05:22 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:05:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-29 22:04:49 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-29 22:04:42 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.031 |  |
| 2026-04-29 22:04:35 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-29 22:03:50 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:03:36 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:03:33 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:03:26 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 22:03:24 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-04-29 22:03:08 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:02:52 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:02:33 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-29 22:02:29 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-04-29 22:02:24 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-29 22:01:54 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:01:21 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:01:14 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-29 22:01:11 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-29 22:00:59 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:00:34 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.050 |  |
| 2026-04-29 22:00:23 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 22:03:24 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-04-29 22:09:21 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-29 22:05:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-29 22:02:33 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-29 22:04:35 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-29 22:00:23 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-29 22:03:26 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 22:09:32 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 22:08:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:00:59 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:02:52 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-29 21:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:01:54 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:06:15 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:03:08 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:01:21 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:11:47 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:03:33 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 21:02:20 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:03:50 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:03:36 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:05:22 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-04-29 22:08:48 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-04-29 22:04:49 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-29 22:01:14 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-29 22:06:05 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-29 22:01:11 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-29 22:02:24 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-29 22:02:29 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-04-29 21:06:11 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.022 |  |
| 2026-04-29 22:04:42 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.031 |  |
| 2026-04-29 22:09:23 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.036 |  |
| 2026-04-29 22:15:10 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.037 |  |
| 2026-04-29 22:13:08 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.046 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-29 22:00:34 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)