# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_19:27:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,607 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 19:27:49 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.700 |  |
| 2026-01-14 19:26:12 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:19:01 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:18:08 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2026-01-14 19:14:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-14 19:12:27 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-14 19:07:54 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:07:53 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:07:01 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-14 19:06:55 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:06:48 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:06:01 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-14 19:05:37 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-14 19:05:29 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:05:29 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-14 19:05:26 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-14 19:05:00 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:04:32 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-14 19:04:25 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:04:22 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 19:03:52 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:03:17 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:03:15 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-01-14 19:03:14 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-01-14 19:02:47 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | -0.060 |  |
| 2026-01-14 19:02:15 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:52 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:44 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:40 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:40 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-01-14 19:01:30 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.030 |  |
| 2026-01-14 19:01:22 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:20 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:16 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-14 19:01:15 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:03 | Horowpothana (Yan Oya) | 2.91 | 🟢 Normal | -0.051 |  |
| 2026-01-14 19:00:15 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 19:18:08 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2026-01-14 19:01:40 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-01-14 19:06:01 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-14 19:14:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-14 19:05:29 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-14 19:12:27 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-14 19:05:37 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-14 19:04:22 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 19:05:26 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-14 18:00:19 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:22 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:04:25 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:52 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:19:01 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:40 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:03:17 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:02:15 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:05:00 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:06:55 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:15 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:07:53 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:00:15 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:06:48 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:07:54 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:44 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:26:12 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:05:29 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:01:20 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 19:04:32 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-14 19:01:16 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-14 19:07:01 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-14 19:03:14 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-01-14 18:02:52 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-01-14 19:03:15 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-01-14 19:01:30 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.030 |  |
| 2026-01-14 19:01:03 | Horowpothana (Yan Oya) | 2.91 | 🟢 Normal | -0.051 |  |
| 2026-01-14 19:02:47 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | -0.060 |  |
| 2026-01-14 19:27:49 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.700 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)