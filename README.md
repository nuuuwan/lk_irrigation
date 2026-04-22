# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_06:02:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,685 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 06:02:36 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.060 |  |
| 2026-04-22 06:02:27 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-22 06:02:03 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-22 06:01:59 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:01:32 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-22 06:01:19 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.038 |  |
| 2026-04-22 06:01:09 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 06:00:30 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.022 |  |
| 2026-04-22 06:00:25 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.071 |  |
| 2026-04-22 05:59:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.064 |  |
| 2026-04-22 05:26:58 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.104 |  |
| 2026-04-22 05:13:52 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.038 |  |
| 2026-04-22 05:11:18 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:11:17 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:11:16 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:11:15 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:11:14 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:11:09 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.005 |  |
| 2026-04-22 05:11:01 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-22 05:09:53 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.029 |  |
| 2026-04-22 05:09:42 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 05:04:04 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-04-22 05:03:40 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-22 05:04:00 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-22 06:02:03 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-22 06:02:27 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-22 05:11:01 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-22 05:02:03 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-22 06:01:09 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 05:02:46 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 05:08:07 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-22 04:19:21 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-22 06:01:59 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:02:27 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:11:18 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:03:59 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:07:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:06:26 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-22 06:01:19 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:11:09 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.005 |  |
| 2026-04-22 05:05:08 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.005 |  |
| 2026-04-22 05:07:36 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-22 05:02:28 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-22 05:04:35 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-22 06:01:32 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-22 06:00:30 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.022 |  |
| 2026-04-22 05:09:53 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.029 |  |
| 2026-04-22 06:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.038 |  |
| 2026-04-22 05:05:00 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-04-22 05:05:05 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.053 |  |
| 2026-04-22 06:02:36 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.060 |  |
| 2026-04-22 05:59:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.064 |  |
| 2026-04-22 05:00:15 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.067 |  |
| 2026-04-22 06:00:25 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.071 |  |
| 2026-04-22 05:02:43 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.099 |  |
| 2026-04-22 05:26:58 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.104 |  |
| 2026-04-22 05:05:16 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | -0.246 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)