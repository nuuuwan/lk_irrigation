# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_11:14:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,310 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 11:14:57 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.017 |  |
| 2026-06-12 11:08:31 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.049 |  |
| 2026-06-12 11:07:36 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-12 11:07:25 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.036 |  |
| 2026-06-12 11:07:18 | Thawalama (Gin Ganga) | 3.47 | 🟢 Normal | -0.084 |  |
| 2026-06-12 11:07:11 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-12 11:07:06 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 11:07:05 | Holombuwa (Kelani Ganga) | 1.47 | 🟢 Normal | -0.092 |  |
| 2026-06-12 11:07:03 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:06:02 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-12 11:05:47 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:05:44 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:05:31 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.030 |  |
| 2026-06-12 11:04:59 | Moraketiya (Walawe Ganga) | 1.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 11:04:27 | Glencourse (Kelani Ganga) | 12.12 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:04:10 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.030 |  |
| 2026-06-12 11:04:06 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-06-12 11:04:03 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-12 11:04:00 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:03:43 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-06-12 11:03:34 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 11:03:33 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:03:22 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-06-12 11:03:18 | Rathnapura (Kalu Ganga) | 5.66 | 🟡 Alert | -0.136 |  |
| 2026-06-12 11:03:14 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-12 11:03:10 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 11:03:03 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:02:54 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:02:52 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-12 11:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.60 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-06-12 11:02:39 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-06-12 11:02:37 | Putupaula (Kalu Ganga) | 1.94 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-12 11:02:32 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:02:27 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-12 11:02:19 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-06-12 11:02:06 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.020 |  |
| 2026-06-12 11:02:04 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:01:33 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 11:00:32 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:00:24 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 10:38:57 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | 0.128 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 11:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.60 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-06-12 11:03:43 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-06-12 11:03:18 | Rathnapura (Kalu Ganga) | 5.66 | 🟡 Alert | -0.136 |  |
| 2026-06-12 11:02:19 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-06-12 11:07:11 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-12 11:02:52 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-12 11:04:03 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-12 11:03:14 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-12 11:06:02 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-12 11:02:37 | Putupaula (Kalu Ganga) | 1.94 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-12 11:02:27 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-12 11:07:36 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-12 11:03:10 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 11:07:06 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 11:03:34 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 11:01:33 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 11:04:59 | Moraketiya (Walawe Ganga) | 1.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-12 11:00:24 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:02:54 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:04:00 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:00:32 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:04:27 | Glencourse (Kelani Ganga) | 12.12 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:03:03 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:02:32 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:02:04 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:05:47 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:05:44 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:07:03 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-12 11:02:39 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-06-12 11:04:06 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-06-12 11:14:57 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.017 |  |
| 2026-06-12 11:02:06 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.020 |  |
| 2026-06-12 11:04:10 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.030 |  |
| 2026-06-12 11:05:31 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.030 |  |
| 2026-06-12 11:07:25 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.036 |  |
| 2026-06-12 11:08:31 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.049 |  |
| 2026-06-12 11:03:22 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-06-12 11:07:18 | Thawalama (Gin Ganga) | 3.47 | 🟢 Normal | -0.084 |  |
| 2026-06-12 11:07:05 | Holombuwa (Kelani Ganga) | 1.47 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)