# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_01:09:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,926 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 01:09:51 | Glencourse (Kelani Ganga) | 12.09 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-12 01:09:11 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-06-12 01:08:22 | Rathnapura (Kalu Ganga) | 5.60 | 🟡 Alert | -0.009 |  |
| 2026-06-12 01:08:12 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-12 01:07:38 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-12 01:07:38 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-12 01:06:59 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-12 01:06:44 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-06-12 01:06:33 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 01:06:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-12 01:05:59 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-12 01:05:21 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-12 01:04:53 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-12 01:04:43 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-06-12 01:04:23 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.108 |  |
| 2026-06-12 01:04:09 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 01:04:06 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-12 01:03:41 | Thawalama (Gin Ganga) | 3.09 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-12 01:03:36 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-12 01:03:08 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-06-12 01:02:38 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-12 01:02:25 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 01:01:38 | Peradeniya (Mahaweli Ganga) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 01:01:26 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2026-06-12 01:01:19 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 00:46:30 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-12 00:35:59 | Magura (Kalu Ganga) | 3.56 | 🟢 Normal | 0.195 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 01:08:22 | Rathnapura (Kalu Ganga) | 5.60 | 🟡 Alert | -0.009 |  |
| 2026-06-12 01:04:43 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-06-12 00:35:59 | Magura (Kalu Ganga) | 3.56 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-06-12 00:00:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.38 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-06-12 01:09:11 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-06-12 01:07:38 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-12 01:04:53 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-12 01:03:41 | Thawalama (Gin Ganga) | 3.09 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-12 01:09:51 | Glencourse (Kelani Ganga) | 12.09 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-12 01:03:36 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-12 01:05:59 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-11 22:08:37 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-12 01:04:06 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-11 23:11:35 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-12 00:03:01 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-12 01:01:38 | Peradeniya (Mahaweli Ganga) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 01:06:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-12 01:04:09 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 01:02:25 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 01:08:12 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-12 01:06:59 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-12 01:06:33 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 01:01:19 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 01:07:38 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-12 00:05:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 00:07:13 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:11:49 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-12 00:02:42 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 00:01:14 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-12 01:02:38 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:01:15 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 01:05:21 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-11 23:11:02 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 00:04:37 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | -0.010 |  |
| 2026-06-12 01:06:44 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-06-12 01:03:08 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-06-11 18:00:24 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.021 |  |
| 2026-06-12 01:01:26 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2026-06-12 01:04:23 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)