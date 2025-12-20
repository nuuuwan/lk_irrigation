# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_11:43:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,017 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 11:43:25 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:26:03 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:13:43 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:12:46 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.025 |  |
| 2025-12-20 11:09:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:07:19 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.010 |  |
| 2025-12-20 11:06:55 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | -0.047 |  |
| 2025-12-20 11:06:37 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.019 |  |
| 2025-12-20 11:06:25 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:06:19 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.029 |  |
| 2025-12-20 11:05:41 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:05:15 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.216 |  |
| 2025-12-20 11:04:49 | Weraganthota (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.040 |  |
| 2025-12-20 11:04:36 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.020 |  |
| 2025-12-20 11:03:41 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:03:27 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 11:03:26 | Thanthirimale (Malwathu Oya) | 5.50 | 🟡 Alert | -0.049 |  |
| 2025-12-20 11:03:24 | Galgamuwa (Mee Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:03:03 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2025-12-20 11:02:52 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-20 11:02:39 | Horowpothana (Yan Oya) | 6.30 | 🟡 Alert | -0.086 |  |
| 2025-12-20 11:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2025-12-20 11:02:34 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-20 11:02:34 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2025-12-20 11:02:32 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:02:21 | Manampitiya (Mahaweli Ganga) | 3.92 | 🟡 Alert | -0.080 |  |
| 2025-12-20 11:02:13 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:02:11 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:02:05 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:02:04 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:02:00 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-20 11:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:01:52 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-20 11:01:50 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.021 |  |
| 2025-12-20 11:01:43 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:01:39 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:01:10 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:01:02 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:01:00 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 10:55:41 | Horowpothana (Yan Oya) | 6.31 | 🟡 Alert | -0.086 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 11:03:26 | Thanthirimale (Malwathu Oya) | 5.50 | 🟡 Alert | -0.049 |  |
| 2025-12-20 11:02:21 | Manampitiya (Mahaweli Ganga) | 3.92 | 🟡 Alert | -0.080 |  |
| 2025-12-20 11:02:39 | Horowpothana (Yan Oya) | 6.30 | 🟡 Alert | -0.086 |  |
| 2025-12-20 11:01:00 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 11:03:27 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 11:02:05 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:01:43 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:02:13 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:03:24 | Galgamuwa (Mee Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:13:43 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:01:39 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:01:10 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:26:03 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:09:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:01:02 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:03:41 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:02:32 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:05:41 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:43:25 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:02:04 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:06:25 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:02:11 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 11:07:19 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.010 |  |
| 2025-12-20 11:02:00 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-20 11:02:52 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-20 11:02:34 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-20 11:01:52 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-20 11:06:37 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.019 |  |
| 2025-12-20 11:04:36 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.020 |  |
| 2025-12-20 11:02:34 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2025-12-20 11:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2025-12-20 11:03:03 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2025-12-20 11:01:50 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.021 |  |
| 2025-12-20 11:12:46 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.025 |  |
| 2025-12-20 11:06:19 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.029 |  |
| 2025-12-20 11:04:49 | Weraganthota (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.040 |  |
| 2025-12-20 11:06:55 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | -0.047 |  |
| 2025-12-20 11:05:15 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.216 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)