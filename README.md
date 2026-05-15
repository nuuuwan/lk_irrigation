# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_08:12:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,314 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 08:12:41 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-15 08:09:32 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.321 |  |
| 2026-05-15 08:08:57 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 08:07:48 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.070 |  |
| 2026-05-15 08:07:29 | Horowpothana (Yan Oya) | 2.91 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-15 08:07:17 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.042 |  |
| 2026-05-15 08:07:16 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | -0.012 |  |
| 2026-05-15 08:07:00 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:06:26 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-05-15 08:06:21 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.066 |  |
| 2026-05-15 08:05:50 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:05:32 | Peradeniya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.011 |  |
| 2026-05-15 08:05:15 | Badalgama (Maha Oya) | 4.66 | 🟢 Normal | -0.063 |  |
| 2026-05-15 08:05:03 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | -0.038 |  |
| 2026-05-15 08:04:53 | Glencourse (Kelani Ganga) | 13.41 | 🟢 Normal | -0.184 |  |
| 2026-05-15 08:04:31 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:04:27 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-05-15 08:04:21 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:04:12 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:03:55 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 08:03:51 | Dunamale (Aththanagalu Oya) | 4.72 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-15 08:03:49 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-05-15 08:03:27 | Putupaula (Kalu Ganga) | 2.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 08:03:27 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-15 08:03:19 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.049 |  |
| 2026-05-15 08:03:05 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 08:03:02 | Hanwella (Kelani Ganga) | 6.17 | 🟢 Normal | -0.042 |  |
| 2026-05-15 08:02:24 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:02:21 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:02:19 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-05-15 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.89 | 🟠 Minor Flood | 0.054 | 🔺 Rising |
| 2026-05-15 08:01:59 | Giriulla (Maha Oya) | 3.59 | 🟢 Normal | -0.061 |  |
| 2026-05-15 08:01:48 | Galgamuwa (Mee Oya) | 3.43 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-15 08:01:40 | Thanthirimale (Malwathu Oya) | 3.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-15 08:01:19 | Katharagama (Menik Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-05-15 08:00:49 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-05-15 08:00:16 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.020 |  |
| 2026-05-15 08:00:07 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-15 07:47:08 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.321 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.89 | 🟠 Minor Flood | 0.054 | 🔺 Rising |
| 2026-05-15 08:03:51 | Dunamale (Aththanagalu Oya) | 4.72 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-15 08:07:16 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | -0.012 |  |
| 2026-05-15 08:01:48 | Galgamuwa (Mee Oya) | 3.43 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-15 08:12:41 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-15 08:03:27 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-15 08:01:40 | Thanthirimale (Malwathu Oya) | 3.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-15 08:03:05 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 08:08:57 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 08:07:29 | Horowpothana (Yan Oya) | 2.91 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-15 08:03:55 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 08:03:27 | Putupaula (Kalu Ganga) | 2.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 08:02:24 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:00:07 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:04:12 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:05:50 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:07:00 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:01:19 | Katharagama (Menik Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:04:21 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:04:31 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:02:21 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-15 08:06:26 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-05-15 08:00:49 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-05-15 08:02:19 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-05-15 08:05:32 | Peradeniya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.011 |  |
| 2026-05-15 08:04:27 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-05-15 08:03:49 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-05-15 08:00:16 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.020 |  |
| 2026-05-15 08:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-05-15 08:05:03 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | -0.038 |  |
| 2026-05-15 08:03:02 | Hanwella (Kelani Ganga) | 6.17 | 🟢 Normal | -0.042 |  |
| 2026-05-15 08:07:17 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.042 |  |
| 2026-05-15 08:03:19 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.049 |  |
| 2026-05-15 08:01:59 | Giriulla (Maha Oya) | 3.59 | 🟢 Normal | -0.061 |  |
| 2026-05-15 08:05:15 | Badalgama (Maha Oya) | 4.66 | 🟢 Normal | -0.063 |  |
| 2026-05-15 08:06:21 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.066 |  |
| 2026-05-15 08:07:48 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.070 |  |
| 2026-05-15 08:04:53 | Glencourse (Kelani Ganga) | 13.41 | 🟢 Normal | -0.184 |  |
| 2026-05-15 08:09:32 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.321 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)