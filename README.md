# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_16:38:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,890 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 16:38:34 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:29:57 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:26:27 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:17:48 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.072 |  |
| 2026-05-22 16:15:45 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:14:08 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-22 16:12:48 | Magura (Kalu Ganga) | 4.45 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-05-22 16:08:46 | Dunamale (Aththanagalu Oya) | 5.08 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-05-22 16:08:14 | Nagalagam Street (Kelani Ganga) | 1.40 | 🟡 Alert | 0.045 | 🔺 Rising |
| 2026-05-22 16:07:32 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-05-22 16:07:30 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-22 16:07:15 | Glencourse (Kelani Ganga) | 15.35 | 🟡 Alert | -0.079 |  |
| 2026-05-22 16:06:04 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:05:30 | Hanwella (Kelani Ganga) | 8.14 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-22 16:05:15 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | -0.328 |  |
| 2026-05-22 16:04:47 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:04:36 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:04:34 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:04:20 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:03:40 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.013 |  |
| 2026-05-22 16:03:32 | Rathnapura (Kalu Ganga) | 7.65 | 🟠 Minor Flood | -0.090 |  |
| 2026-05-22 16:03:07 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:02:47 | Ellagawa (Kalu Ganga) | 9.31 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-22 16:02:40 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-22 16:02:38 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-22 16:02:33 | Badalgama (Maha Oya) | 3.92 | 🟢 Normal | -0.049 |  |
| 2026-05-22 16:02:32 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.71 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-05-22 16:02:25 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.110 |  |
| 2026-05-22 16:02:16 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:02:14 | Putupaula (Kalu Ganga) | 2.33 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-22 16:01:55 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-05-22 16:01:53 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:01:44 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-22 16:01:40 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:01:31 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-05-22 16:00:57 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 16:00:47 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-05-22 16:00:26 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 16:08:46 | Dunamale (Aththanagalu Oya) | 5.08 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-05-22 16:05:30 | Hanwella (Kelani Ganga) | 8.14 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-22 16:03:32 | Rathnapura (Kalu Ganga) | 7.65 | 🟠 Minor Flood | -0.090 |  |
| 2026-05-22 16:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.71 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2026-05-22 16:08:14 | Nagalagam Street (Kelani Ganga) | 1.40 | 🟡 Alert | 0.045 | 🔺 Rising |
| 2026-05-22 16:12:48 | Magura (Kalu Ganga) | 4.45 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-05-22 16:07:15 | Glencourse (Kelani Ganga) | 15.35 | 🟡 Alert | -0.079 |  |
| 2026-05-22 16:14:08 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-05-22 16:02:38 | Giriulla (Maha Oya) | 1.99 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-22 16:02:14 | Putupaula (Kalu Ganga) | 2.33 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-22 16:02:47 | Ellagawa (Kalu Ganga) | 9.31 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-22 16:07:30 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-22 16:02:40 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-22 16:00:57 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 16:01:53 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:00:26 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:01:40 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:03:07 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:01:03 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:02:32 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:15:45 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:29:57 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:00:13 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:06:04 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:04:34 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:02:16 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:04:36 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:38:34 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:00:47 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 16:01:55 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-05-22 16:07:32 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-05-22 16:01:31 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-05-22 16:01:44 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-22 16:03:40 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.013 |  |
| 2026-05-22 16:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-05-22 16:02:33 | Badalgama (Maha Oya) | 3.92 | 🟢 Normal | -0.049 |  |
| 2026-05-22 16:17:48 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.072 |  |
| 2026-05-22 16:02:25 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.110 |  |
| 2026-05-22 16:05:15 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | -0.328 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)