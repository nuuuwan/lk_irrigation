# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_15:09:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,042 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 15:09:26 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.046 |  |
| 2026-04-13 15:07:55 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:07:44 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-04-13 15:07:05 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:06:56 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-13 15:06:41 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.021 |  |
| 2026-04-13 15:06:33 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.019 |  |
| 2026-04-13 15:05:56 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-13 15:05:52 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.234 |  |
| 2026-04-13 15:05:34 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:05:34 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.014 |  |
| 2026-04-13 15:05:22 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.058 |  |
| 2026-04-13 15:05:11 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-04-13 15:04:58 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.029 |  |
| 2026-04-13 15:04:58 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.175 |  |
| 2026-04-13 15:04:47 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-04-13 15:04:41 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:04:23 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:04:20 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 15:04:19 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:04:11 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:03:44 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-13 15:03:36 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-04-13 15:03:29 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:03:24 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.030 |  |
| 2026-04-13 15:02:59 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:02:30 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-13 15:02:25 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:02:23 | Katharagama (Menik Ganga) | -0.60 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-13 15:02:22 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 15:02:16 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-13 15:02:06 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:02:02 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.107 |  |
| 2026-04-13 15:01:48 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 15:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:01:23 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.083 |  |
| 2026-04-13 15:01:13 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:01:08 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:00:57 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.035 |  |
| 2026-04-13 15:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-13 14:57:00 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 15:02:23 | Katharagama (Menik Ganga) | -0.60 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-13 15:02:30 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-13 15:01:48 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 15:05:56 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-13 15:03:44 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-13 15:06:56 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-13 15:02:22 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 15:04:20 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 15:02:25 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:04:41 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:04:23 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:05:34 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:04:19 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:07:55 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:07:05 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:02:59 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:02:06 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:03:29 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:04:11 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:01:13 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-13 15:02:16 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-13 15:05:34 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.014 |  |
| 2026-04-13 15:05:11 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-04-13 15:06:33 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.019 |  |
| 2026-04-13 15:07:44 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-04-13 15:04:47 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-04-13 15:06:41 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.021 |  |
| 2026-04-13 15:04:58 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.029 |  |
| 2026-04-13 15:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.030 |  |
| 2026-04-13 15:03:36 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-04-13 15:00:57 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.035 |  |
| 2026-04-13 15:09:26 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.046 |  |
| 2026-04-13 15:05:22 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.058 |  |
| 2026-04-13 15:01:23 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.083 |  |
| 2026-04-13 15:02:02 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.107 |  |
| 2026-04-13 15:04:58 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.175 |  |
| 2026-04-13 15:05:52 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)