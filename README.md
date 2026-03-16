# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_12:15:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,901 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 12:15:33 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:11:46 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:11:34 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-03-16 12:11:28 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:11:16 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:08:49 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:07:54 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:07:15 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-03-16 12:06:37 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:06:08 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.063 |  |
| 2026-03-16 12:06:04 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-16 12:05:11 | Baddegama (Gin Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:05:06 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:04:29 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:04:24 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 12:03:29 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-03-16 12:00:21 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-16 12:01:53 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-16 12:06:04 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-16 12:02:48 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-16 12:03:44 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 12:03:32 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 12:05:06 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:01:35 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:02:53 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:11:16 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:03:48 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:15:33 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:02:32 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:01:19 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:05:11 | Baddegama (Gin Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:08:49 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:11:28 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:07:54 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:04:24 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:04:29 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:06:37 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:02:38 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:00:09 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-16 12:07:15 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-03-16 12:02:59 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-03-16 12:02:21 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-16 12:02:24 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-16 12:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-03-16 12:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-03-16 12:02:39 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-03-16 12:00:45 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-03-16 12:11:34 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.021 |  |
| 2026-03-16 12:02:08 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-03-16 12:00:30 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.032 |  |
| 2026-03-16 12:06:08 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.063 |  |
| 2026-03-16 12:03:59 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.104 |  |
| 2026-03-16 12:00:40 | Weraganthota (Mahaweli Ganga) | -2.31 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)