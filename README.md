# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_23:14:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,540 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 23:14:01 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-06-14 23:11:26 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-14 23:10:23 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.030 |  |
| 2026-06-14 23:10:17 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-06-14 23:06:54 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-14 23:06:44 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:06:42 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.093 |  |
| 2026-06-14 23:06:25 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-14 23:06:14 | Putupaula (Kalu Ganga) | 2.55 | 🟢 Normal | -0.022 |  |
| 2026-06-14 23:05:47 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:05:31 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-14 23:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | -0.009 |  |
| 2026-06-14 23:05:21 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | 3.242 | 🔺 Rising |
| 2026-06-14 23:04:53 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-14 23:03:54 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-06-14 23:03:42 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-06-14 23:03:31 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:03:30 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:03:17 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-06-14 23:03:08 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | -0.124 |  |
| 2026-06-14 23:02:14 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-06-14 23:02:12 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-06-14 23:01:57 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 23:01:52 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-06-14 23:01:48 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-06-14 23:01:20 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:01:15 | Ellagawa (Kalu Ganga) | 7.53 | 🟢 Normal | -0.091 |  |
| 2026-06-14 23:01:14 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:00:59 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.021 |  |
| 2026-06-14 23:00:25 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 23:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | -0.009 |  |
| 2026-06-14 23:05:21 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | 3.242 | 🔺 Rising |
| 2026-06-14 23:02:14 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-06-14 23:06:25 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-14 23:05:31 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-14 23:11:26 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-14 23:01:57 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 23:06:54 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-14 23:00:25 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:01:14 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:01:53 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:05:47 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:03:45 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:03:30 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:06:44 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:01:41 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:03:31 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 23:01:20 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-14 22:17:25 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.008 |  |
| 2026-06-14 22:16:48 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.008 |  |
| 2026-06-14 18:04:23 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-06-14 23:10:17 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-14 23:01:52 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-06-14 23:04:53 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-14 23:03:54 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-06-14 23:14:01 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-06-14 22:03:45 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-06-14 23:01:48 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-06-14 18:03:42 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-14 23:03:17 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-06-14 23:00:59 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.021 |  |
| 2026-06-14 23:06:14 | Putupaula (Kalu Ganga) | 2.55 | 🟢 Normal | -0.022 |  |
| 2026-06-14 23:10:23 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.030 |  |
| 2026-06-14 23:03:42 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-06-14 23:02:12 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.040 |  |
| 2026-06-14 23:01:15 | Ellagawa (Kalu Ganga) | 7.53 | 🟢 Normal | -0.091 |  |
| 2026-06-14 23:06:42 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.093 |  |
| 2026-06-14 23:03:08 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)