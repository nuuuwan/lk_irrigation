# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_17:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,538 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 17:13:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-12 17:12:00 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.043 |  |
| 2026-06-12 17:10:04 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.048 |  |
| 2026-06-12 17:09:37 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:09:17 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | -0.010 |  |
| 2026-06-12 17:07:42 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-12 17:07:41 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-06-12 17:07:08 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-06-12 17:06:58 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-12 17:06:56 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-12 17:06:30 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:06:29 | Giriulla (Maha Oya) | 2.46 | 🟢 Normal | -0.019 |  |
| 2026-06-12 17:06:26 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-06-12 17:06:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.087 |  |
| 2026-06-12 17:05:54 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-06-12 17:05:11 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:05:08 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 17:04:59 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:04:12 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:03:58 | Thawalama (Gin Ganga) | 2.91 | 🟢 Normal | -0.032 |  |
| 2026-06-12 17:03:46 | Hanwella (Kelani Ganga) | 3.97 | 🟢 Normal | -0.030 |  |
| 2026-06-12 17:03:44 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | -0.072 |  |
| 2026-06-12 17:03:44 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.048 |  |
| 2026-06-12 17:03:29 | Rathnapura (Kalu Ganga) | 5.55 | 🟡 Alert | 0.193 | 🔺 Rising |
| 2026-06-12 17:03:07 | Deraniyagala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-12 17:03:04 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-06-12 17:02:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:02:51 | Moraketiya (Walawe Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-12 17:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-06-12 17:02:21 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 17:02:19 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-12 17:02:17 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-12 17:02:00 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-12 17:00:35 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:00:20 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:00:09 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 16:28:59 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | 24.000 | 🔺 Rising |
| 2026-06-12 16:28:56 | Baddegama (Gin Ganga) | 2.79 | 🟢 Normal | 24.000 | 🔺 Rising |
| 2026-06-12 16:26:03 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 17:03:29 | Rathnapura (Kalu Ganga) | 5.55 | 🟡 Alert | 0.193 | 🔺 Rising |
| 2026-06-12 17:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-06-12 17:03:44 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.048 |  |
| 2026-06-12 16:28:59 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | 24.000 | 🔺 Rising |
| 2026-06-12 17:06:26 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-06-12 17:07:41 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-06-12 17:05:54 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-06-12 17:07:08 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-06-12 17:06:56 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-12 17:03:07 | Deraniyagala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-12 17:06:58 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-12 17:07:42 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-12 17:02:00 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-12 17:05:08 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 17:13:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-12 17:02:17 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-12 17:02:19 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-12 17:02:21 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 17:00:35 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:00:20 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:04:59 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:00:09 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:06:30 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:09:37 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:05:11 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:02:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-12 15:02:59 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:04:12 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-06-12 16:26:03 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-06-12 17:09:17 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | -0.010 |  |
| 2026-06-12 17:03:04 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-06-12 17:02:51 | Moraketiya (Walawe Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-12 17:06:29 | Giriulla (Maha Oya) | 2.46 | 🟢 Normal | -0.019 |  |
| 2026-06-12 17:03:46 | Hanwella (Kelani Ganga) | 3.97 | 🟢 Normal | -0.030 |  |
| 2026-06-12 17:03:58 | Thawalama (Gin Ganga) | 2.91 | 🟢 Normal | -0.032 |  |
| 2026-06-12 17:12:00 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.043 |  |
| 2026-06-12 17:10:04 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.048 |  |
| 2026-06-12 17:03:44 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | -0.072 |  |
| 2026-06-12 17:06:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)