# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_09:06:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,145 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 09:06:21 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:06:12 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:06:08 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-22 09:05:31 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-22 09:05:01 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:04:40 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:04:31 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-22 09:04:30 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-22 09:04:29 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.062 |  |
| 2026-03-22 09:04:17 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.019 |  |
| 2026-03-22 09:03:40 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:03:27 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:03:24 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.392 |  |
| 2026-03-22 09:03:22 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2026-03-22 09:03:17 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-22 09:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:02:34 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.066 |  |
| 2026-03-22 09:02:30 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:02:23 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:02:19 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-03-22 09:02:09 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:01:46 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.040 |  |
| 2026-03-22 09:01:38 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:01:31 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:01:26 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.053 |  |
| 2026-03-22 09:01:11 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:01:10 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:01:08 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.120 |  |
| 2026-03-22 09:01:05 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-03-22 09:00:55 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-03-22 08:26:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:24:36 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:15:22 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:13:13 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 09:01:05 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-03-22 09:04:30 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-22 09:05:31 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-22 09:03:17 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-22 08:05:47 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-22 09:04:31 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-22 08:05:04 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 09:01:31 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:01:11 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:01:15 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:01:38 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:03:40 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:15:22 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:02:23 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:04:40 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:06:12 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:02:09 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:13:13 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:03:27 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:00:55 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:06:21 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:05:01 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:02:30 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:01:10 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 09:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 08:03:29 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-03-22 09:06:08 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-22 09:02:19 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-03-22 08:10:58 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.013 |  |
| 2026-03-22 09:04:17 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.019 |  |
| 2026-03-22 09:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-03-22 09:01:46 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.040 |  |
| 2026-03-22 08:02:42 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2026-03-22 09:03:22 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.052 |  |
| 2026-03-22 09:01:26 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.053 |  |
| 2026-03-22 09:04:29 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.062 |  |
| 2026-03-22 09:02:34 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.066 |  |
| 2026-03-22 09:01:08 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.120 |  |
| 2026-03-22 09:03:24 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.392 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)