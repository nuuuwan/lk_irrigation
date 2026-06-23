# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_06:12:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,928 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 06:12:53 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-23 06:09:40 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:09:23 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-23 06:08:39 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.087 |  |
| 2026-06-23 06:08:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-06-23 06:08:31 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.080 |  |
| 2026-06-23 06:07:35 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.131 |  |
| 2026-06-23 06:06:36 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | 0.033 | 🔺 Rising |
| 2026-06-23 06:06:07 | Badalgama (Maha Oya) | 3.63 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-23 06:05:30 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-23 06:05:18 | Deraniyagala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.734 |  |
| 2026-06-23 06:05:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:05:11 | Glencourse (Kelani Ganga) | 13.20 | 🟢 Normal | -0.108 |  |
| 2026-06-23 06:04:56 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | -0.089 |  |
| 2026-06-23 06:04:37 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-06-23 06:04:31 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:04:29 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:04:23 | Dunamale (Aththanagalu Oya) | 4.00 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-06-23 06:04:21 | Ellagawa (Kalu Ganga) | 7.97 | 🟢 Normal | -0.031 |  |
| 2026-06-23 06:03:29 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 06:02:36 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:02:33 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.314 |  |
| 2026-06-23 06:02:17 | Hanwella (Kelani Ganga) | 4.97 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-23 06:01:57 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | -0.013 |  |
| 2026-06-23 06:01:52 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-23 06:01:43 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.061 |  |
| 2026-06-23 06:01:20 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-23 06:01:17 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-23 06:01:12 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:01:10 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:01:07 | Giriulla (Maha Oya) | 2.81 | 🟢 Normal | -0.033 |  |
| 2026-06-23 06:01:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-23 06:00:44 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-23 06:00:30 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-23 06:00:30 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 06:04:23 | Dunamale (Aththanagalu Oya) | 4.00 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-06-23 06:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | 0.033 | 🔺 Rising |
| 2026-06-23 06:01:57 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | -0.013 |  |
| 2026-06-23 06:06:07 | Badalgama (Maha Oya) | 3.63 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-23 06:09:23 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-23 06:12:53 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-23 06:00:10 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-23 06:02:17 | Hanwella (Kelani Ganga) | 4.97 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-23 06:01:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-23 06:00:30 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-23 06:00:44 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-23 06:05:30 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-23 06:01:17 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-23 06:03:29 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 06:01:20 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-23 06:04:31 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:01:10 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:06:36 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:09:40 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:01:12 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:05:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:01:43 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:04:29 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:55 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:02:36 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-23 06:08:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-06-23 06:01:52 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-23 06:00:30 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-23 06:04:37 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-06-23 06:04:21 | Ellagawa (Kalu Ganga) | 7.97 | 🟢 Normal | -0.031 |  |
| 2026-06-23 06:01:07 | Giriulla (Maha Oya) | 2.81 | 🟢 Normal | -0.033 |  |
| 2026-06-23 06:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.061 |  |
| 2026-06-23 06:08:31 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.080 |  |
| 2026-06-23 06:08:39 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.087 |  |
| 2026-06-23 06:04:56 | Rathnapura (Kalu Ganga) | 3.88 | 🟢 Normal | -0.089 |  |
| 2026-06-23 06:05:11 | Glencourse (Kelani Ganga) | 13.20 | 🟢 Normal | -0.108 |  |
| 2026-06-23 06:07:35 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.131 |  |
| 2026-06-23 06:02:33 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.314 |  |
| 2026-06-23 06:05:18 | Deraniyagala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.734 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)