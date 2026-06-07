# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_18:11:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,111 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 18:11:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-07 18:11:13 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:08:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:08:07 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 18:07:51 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:07:38 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:07:24 | Magura (Kalu Ganga) | 3.51 | 🟢 Normal | -0.110 |  |
| 2026-06-07 18:06:53 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-07 18:06:14 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 18:06:14 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 18:05:31 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.082 |  |
| 2026-06-07 18:04:26 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-06-07 18:04:21 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-07 18:03:55 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.100 |  |
| 2026-06-07 18:03:54 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:03:45 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | -0.029 |  |
| 2026-06-07 18:03:44 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:03:31 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-07 18:03:23 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:02:51 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.152 |  |
| 2026-06-07 18:02:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:02:46 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.021 |  |
| 2026-06-07 18:02:45 | Rathnapura (Kalu Ganga) | 4.13 | 🟢 Normal | -0.079 |  |
| 2026-06-07 18:02:38 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:02:35 | Ellagawa (Kalu Ganga) | 7.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 18:02:23 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:02:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:02:01 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:01:58 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 18:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-06-07 18:01:40 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 18:01:22 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:01:20 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-07 18:00:48 | Putupaula (Kalu Ganga) | 1.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-07 18:00:28 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 18:01:20 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-07 18:06:53 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-07 18:00:48 | Putupaula (Kalu Ganga) | 1.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-07 18:03:31 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-07 18:01:58 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-07 18:11:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-07 18:01:40 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 18:02:35 | Ellagawa (Kalu Ganga) | 7.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 18:06:14 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 18:03:44 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:06:14 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 18:08:07 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 18:03:23 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:02:23 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:02:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:08:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:07:51 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 17:02:39 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:02:38 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:01:22 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:02:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:02:01 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:07:38 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:03:54 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:11:13 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-07 18:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-06-07 18:00:28 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-07 18:04:26 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-06-07 18:04:21 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-07 18:02:46 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.021 |  |
| 2026-06-07 18:03:45 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | -0.029 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-07 18:02:45 | Rathnapura (Kalu Ganga) | 4.13 | 🟢 Normal | -0.079 |  |
| 2026-06-07 18:05:31 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.082 |  |
| 2026-06-07 18:03:55 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.100 |  |
| 2026-06-07 18:07:24 | Magura (Kalu Ganga) | 3.51 | 🟢 Normal | -0.110 |  |
| 2026-06-07 18:02:51 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)