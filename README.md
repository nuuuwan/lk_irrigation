# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_21:13:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,937 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 21:13:38 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-19 21:09:34 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 21:09:33 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.134 |  |
| 2026-03-19 21:07:40 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-19 21:07:31 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:07:16 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-03-19 21:07:11 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 21:06:36 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:05:43 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-19 21:05:09 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:04:34 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.098 |  |
| 2026-03-19 21:04:23 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-03-19 21:04:21 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:04:07 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:04:00 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-19 21:03:58 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-19 21:03:43 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-19 21:03:34 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-03-19 21:03:30 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:03:25 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:03:20 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.041 |  |
| 2026-03-19 21:03:19 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:03:16 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:03:12 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.097 |  |
| 2026-03-19 21:03:11 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-19 21:02:51 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.257 |  |
| 2026-03-19 21:02:26 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:02:05 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:02:00 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-03-19 21:02:00 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.020 |  |
| 2026-03-19 21:01:50 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:01:20 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-19 21:01:13 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-03-19 21:01:12 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:00:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 21:02:00 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-03-19 21:04:00 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-19 21:07:40 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-19 21:05:43 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-19 21:03:43 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-19 21:07:11 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 21:03:58 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-19 21:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-19 21:13:38 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-19 21:01:20 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-19 21:09:34 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 21:07:31 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:01:50 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:00:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:02:05 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:02:26 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:04:21 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:05:09 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:03:19 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:03:16 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:03:30 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:04:07 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:06:36 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:01:12 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:03:11 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:12:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-03-19 21:07:16 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-03-19 21:03:34 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-03-19 21:01:13 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-03-19 21:04:23 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-03-19 21:02:00 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.020 |  |
| 2026-03-19 21:03:20 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.041 |  |
| 2026-03-19 21:03:12 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.097 |  |
| 2026-03-19 21:04:34 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.098 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-19 21:09:33 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.134 |  |
| 2026-03-19 21:02:51 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.257 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)