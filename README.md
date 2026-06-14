# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_11:16:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,089 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 11:16:38 | Baddegama (Gin Ganga) | 2.77 | 🟢 Normal | -0.034 |  |
| 2026-06-14 11:15:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-14 11:08:53 | Dunamale (Aththanagalu Oya) | 3.08 | 🟢 Normal | -0.020 |  |
| 2026-06-14 11:08:43 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:08:30 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.023 |  |
| 2026-06-14 11:08:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-14 11:08:17 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | -0.020 |  |
| 2026-06-14 11:07:53 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.039 |  |
| 2026-06-14 11:07:21 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.089 |  |
| 2026-06-14 11:06:53 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.039 |  |
| 2026-06-14 11:06:50 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-06-14 11:06:40 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:06:10 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-06-14 11:04:57 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-06-14 11:04:50 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:04:29 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:04:19 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-14 11:04:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-14 11:04:05 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.101 |  |
| 2026-06-14 11:04:01 | Hanwella (Kelani Ganga) | 3.55 | 🟢 Normal | -0.030 |  |
| 2026-06-14 11:03:55 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:03:44 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.040 |  |
| 2026-06-14 11:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | -0.022 |  |
| 2026-06-14 11:03:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.176 |  |
| 2026-06-14 11:03:36 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.088 |  |
| 2026-06-14 11:03:16 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-06-14 11:02:38 | Ellagawa (Kalu Ganga) | 8.39 | 🟢 Normal | -0.029 |  |
| 2026-06-14 11:02:19 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-06-14 11:02:12 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-06-14 11:02:11 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 11:02:09 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-14 11:01:58 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.066 |  |
| 2026-06-14 11:01:58 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-06-14 11:01:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:01:34 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:01:10 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:01:03 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 11:00:38 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 11:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | -0.022 |  |
| 2026-06-14 11:04:19 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-14 11:08:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-14 11:02:09 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-14 11:01:03 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 11:02:11 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 11:15:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-14 11:01:10 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:04:29 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:01:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:08:43 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:01:34 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:03:55 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:04:50 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-14 09:02:49 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:06:40 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-14 11:06:10 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-06-14 11:03:16 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-06-14 11:04:12 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-14 11:01:58 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-06-14 11:06:50 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-06-14 11:08:53 | Dunamale (Aththanagalu Oya) | 3.08 | 🟢 Normal | -0.020 |  |
| 2026-06-14 11:08:17 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | -0.020 |  |
| 2026-06-14 11:02:12 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-06-14 11:04:57 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-06-14 11:08:30 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.023 |  |
| 2026-06-14 11:02:38 | Ellagawa (Kalu Ganga) | 8.39 | 🟢 Normal | -0.029 |  |
| 2026-06-14 11:04:01 | Hanwella (Kelani Ganga) | 3.55 | 🟢 Normal | -0.030 |  |
| 2026-06-14 11:02:19 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-06-14 11:00:38 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.031 |  |
| 2026-06-14 11:16:38 | Baddegama (Gin Ganga) | 2.77 | 🟢 Normal | -0.034 |  |
| 2026-06-14 11:06:53 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.039 |  |
| 2026-06-14 11:07:53 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.039 |  |
| 2026-06-14 11:03:44 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.040 |  |
| 2026-06-14 11:01:58 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.066 |  |
| 2026-06-14 11:03:36 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.088 |  |
| 2026-06-14 11:07:21 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.089 |  |
| 2026-06-14 11:04:05 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.101 |  |
| 2026-06-14 11:03:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.176 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)