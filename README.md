# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_05:07:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,679 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 05:07:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-25 05:07:18 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.009 |  |
| 2026-06-25 05:07:17 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:06:28 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.012 |  |
| 2026-06-25 05:06:20 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-06-25 05:05:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:04:44 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | 2.914 | 🔺 Rising |
| 2026-06-25 05:04:15 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:04:13 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:03:51 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.049 |  |
| 2026-06-25 05:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:03:06 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:02:52 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 05:02:47 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.094 |  |
| 2026-06-25 05:02:41 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.041 |  |
| 2026-06-25 05:02:36 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-06-25 05:02:36 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:02:11 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:02:08 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:01:40 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-25 05:01:38 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:01:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:01:11 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 05:00:58 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 05:00:57 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-06-25 05:00:29 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.104 |  |
| 2026-06-25 04:58:07 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-06-25 04:46:14 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-25 04:45:32 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:41:28 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:19:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 05:04:44 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | 2.914 | 🔺 Rising |
| 2026-06-25 05:02:36 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-06-25 05:01:40 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-25 05:07:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-25 05:00:58 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 05:01:11 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-25 05:02:52 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 04:01:08 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 05:02:11 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:03:06 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:01:38 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:02:36 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:04:15 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:01:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:07:17 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:05:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:04:26 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:03:01 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-25 05:02:08 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 04:19:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-06-25 04:12:10 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-06-25 05:07:18 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.009 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 04:02:25 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-25 05:06:20 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-06-25 05:00:57 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-06-25 05:06:28 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.012 |  |
| 2026-06-25 04:05:19 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.022 |  |
| 2026-06-25 03:05:21 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-06-25 05:02:41 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.041 |  |
| 2026-06-25 05:03:51 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.049 |  |
| 2026-06-25 03:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | -0.056 |  |
| 2026-06-25 05:02:47 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.094 |  |
| 2026-06-25 05:00:29 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.104 |  |
| 2026-06-25 03:08:31 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -5.684 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)