# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_23:28:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,798 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 23:28:34 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-05-16 23:18:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.024 |  |
| 2026-05-16 23:17:21 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-16 23:12:43 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.042 |  |
| 2026-05-16 23:09:26 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:09:17 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:08:59 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.028 |  |
| 2026-05-16 23:07:53 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:07:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 23:07:07 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.009 |  |
| 2026-05-16 23:06:39 | Putupaula (Kalu Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-05-16 23:06:06 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-16 23:05:59 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.029 |  |
| 2026-05-16 23:05:45 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-05-16 23:05:38 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:05:32 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-16 23:03:19 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-16 23:03:11 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:53 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | -0.078 |  |
| 2026-05-16 23:02:45 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:43 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:41 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | -0.079 |  |
| 2026-05-16 23:02:39 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:36 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:26 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:09 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:01:47 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:01:16 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 23:00:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:00:38 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 23:07:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 23:02:41 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | -0.079 |  |
| 2026-05-16 23:17:21 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-16 23:05:32 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 23:01:16 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 23:06:06 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-16 23:05:38 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:45 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:26 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:43 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:36 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:09:17 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:09 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:01:47 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:00:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:00:38 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:05:04 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:03:11 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:09:26 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:07:53 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:39 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:05:45 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-05-16 23:07:07 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.009 |  |
| 2026-05-16 23:03:19 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-16 22:00:11 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-05-16 23:06:39 | Putupaula (Kalu Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-05-16 23:28:34 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-05-16 23:18:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.024 |  |
| 2026-05-16 22:34:34 | Magura (Kalu Ganga) | 3.41 | 🟢 Normal | -0.026 |  |
| 2026-05-16 23:08:59 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.028 |  |
| 2026-05-16 23:05:59 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.029 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-16 21:10:20 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.036 |  |
| 2026-05-16 23:12:43 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.042 |  |
| 2026-05-16 22:01:12 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.047 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-16 23:02:53 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | -0.078 |  |
| 2026-05-16 22:03:37 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)