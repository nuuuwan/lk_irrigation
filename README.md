# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_14:12:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **88,122 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 14:12:31 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-03 14:10:46 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 14:09:13 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-03 14:08:31 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:07:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:07:21 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:06:58 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-03-03 14:06:40 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-03 14:05:35 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:05:22 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:04:59 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:04:53 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-03 14:04:51 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-03-03 14:04:17 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 14:04:16 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-03-03 14:04:05 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 14:04:03 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-03 14:03:57 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:03:53 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:03:46 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:03:34 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:03:05 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-03 14:03:00 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-03 14:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:02:36 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-03-03 14:02:31 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:02:30 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-03 14:02:26 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:02:26 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | -0.090 |  |
| 2026-03-03 14:02:02 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:01:34 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 14:01:30 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:01:13 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-03 14:01:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:00:57 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | -0.357 |  |
| 2026-03-03 14:00:41 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:00:19 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | -0.040 |  |
| 2026-03-03 14:00:10 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:44:46 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-03 13:32:34 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 14:09:13 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-03 14:04:16 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-03-03 14:01:13 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-03 14:04:53 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-03 14:03:05 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-03 14:12:31 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-03 14:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-03 14:04:03 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-03 14:02:30 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-03 14:04:05 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 14:01:34 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 14:04:17 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 14:10:46 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 14:00:10 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:02:02 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:02:31 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:05:22 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:08:31 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:03:53 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:07:21 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:03:34 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:03:46 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:01:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:01:30 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:04:59 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:03:57 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:06:40 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:00:41 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:07:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:02:26 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:05:35 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 14:06:58 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-03-03 14:03:00 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-03 14:02:36 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-03-03 14:04:51 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-03-03 14:00:19 | Weraganthota (Mahaweli Ganga) | -1.74 | 🟢 Normal | -0.040 |  |
| 2026-03-03 14:02:26 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | -0.090 |  |
| 2026-03-03 14:00:57 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | -0.357 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)