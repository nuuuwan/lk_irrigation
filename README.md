# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_07:36:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,600 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 07:36:38 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-29 07:15:49 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.025 |  |
| 2026-05-29 07:15:12 | Baddegama (Gin Ganga) | 3.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-29 07:13:16 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:08:15 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-29 07:07:01 | Panadugama (Nilwala Ganga) | 4.94 | 🟢 Normal | -0.087 |  |
| 2026-05-29 07:06:44 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:06:34 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.085 |  |
| 2026-05-29 07:06:05 | Magura (Kalu Ganga) | 4.48 | 🟡 Alert | -0.067 |  |
| 2026-05-29 07:06:00 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.030 |  |
| 2026-05-29 07:05:57 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:05:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:05:45 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-29 07:05:44 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-05-29 07:05:44 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-29 07:05:37 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:05:37 | Glencourse (Kelani Ganga) | 11.89 | 🟢 Normal | -0.105 |  |
| 2026-05-29 07:05:17 | Hanwella (Kelani Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:05:08 | Rathnapura (Kalu Ganga) | 4.58 | 🟢 Normal | -0.068 |  |
| 2026-05-29 07:05:02 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.002 |  |
| 2026-05-29 07:04:07 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:03:33 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:03:21 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-05-29 07:02:59 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.182 |  |
| 2026-05-29 07:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-29 07:02:34 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-05-29 07:02:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 07:02:29 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:02:21 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 07:02:17 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 07:02:11 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-29 07:02:10 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.040 |  |
| 2026-05-29 07:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-29 07:01:40 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-05-29 07:01:36 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:01:15 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.135 |  |
| 2026-05-29 07:01:11 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-05-29 07:00:53 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-05-29 07:00:10 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 07:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-29 07:06:05 | Magura (Kalu Ganga) | 4.48 | 🟡 Alert | -0.067 |  |
| 2026-05-29 07:03:21 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-05-29 07:01:40 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-05-29 07:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-29 07:05:44 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-29 07:08:15 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-29 07:02:21 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-29 07:05:45 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-29 07:02:17 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 07:02:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 07:15:12 | Baddegama (Gin Ganga) | 3.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-29 07:36:38 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-29 07:05:37 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:03:33 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:02:29 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:06:44 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:04:07 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:00:10 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:13:16 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:05:17 | Hanwella (Kelani Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:05:57 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:05:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:01:36 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-29 07:05:02 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.002 |  |
| 2026-05-29 07:05:44 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-05-29 07:02:11 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-29 07:00:53 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-05-29 07:15:49 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.025 |  |
| 2026-05-29 07:06:00 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.030 |  |
| 2026-05-29 07:01:11 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-05-29 07:02:10 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.040 |  |
| 2026-05-29 07:02:34 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-05-29 07:05:08 | Rathnapura (Kalu Ganga) | 4.58 | 🟢 Normal | -0.068 |  |
| 2026-05-29 07:06:34 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.085 |  |
| 2026-05-29 07:07:01 | Panadugama (Nilwala Ganga) | 4.94 | 🟢 Normal | -0.087 |  |
| 2026-05-29 07:05:37 | Glencourse (Kelani Ganga) | 11.89 | 🟢 Normal | -0.105 |  |
| 2026-05-29 07:01:15 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.135 |  |
| 2026-05-29 07:02:59 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)