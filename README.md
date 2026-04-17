# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_18:06:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,728 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 18:06:49 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:06:12 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:06:07 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-04-17 18:05:38 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:05:23 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:04:42 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.081 |  |
| 2026-04-17 18:04:41 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-04-17 18:04:31 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:04:21 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:04:19 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.030 |  |
| 2026-04-17 18:04:09 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:03:54 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-04-17 18:03:11 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:03:09 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:02:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:54 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:32 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-17 18:02:31 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 18:02:28 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-04-17 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:02:24 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:19 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:12 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 18:02:03 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-17 18:01:43 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-17 18:01:22 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.166 |  |
| 2026-04-17 18:01:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:01:13 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.023 |  |
| 2026-04-17 18:00:41 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:00:41 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:00:35 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:00:13 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 17:20:29 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-17 17:16:54 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 18:02:03 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-17 18:02:32 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-17 17:04:41 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-17 18:02:12 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 18:01:43 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-17 18:00:13 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 18:02:31 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 18:04:21 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:05:38 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:24 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:01:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:00:24 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:08:46 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:03:11 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:04:31 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:00:35 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:06:12 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:00:17 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:00:41 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:06:49 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:19 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 17:07:54 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-04-17 18:05:23 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:03:09 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:04:09 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:00:41 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-17 18:03:54 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-04-17 17:02:25 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.020 |  |
| 2026-04-17 18:06:07 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-04-17 18:01:13 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.023 |  |
| 2026-04-17 18:04:41 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-04-17 18:04:19 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.030 |  |
| 2026-04-17 18:02:28 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-04-17 18:04:42 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.081 |  |
| 2026-04-17 17:07:13 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.149 |  |
| 2026-04-17 18:01:22 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.166 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)