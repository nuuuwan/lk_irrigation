# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_01:15:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,822 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 01:15:08 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-13 01:09:59 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.067 |  |
| 2026-06-13 01:09:00 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.019 |  |
| 2026-06-13 01:08:28 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-13 01:06:31 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-13 01:06:20 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 01:06:10 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-13 01:05:35 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.010 |  |
| 2026-06-13 01:05:23 | Magura (Kalu Ganga) | 4.73 | 🟡 Alert | 0.000 |  |
| 2026-06-13 01:05:08 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-13 01:04:26 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-06-13 01:04:20 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-13 01:04:15 | Pitabeddara (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-13 01:03:47 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-13 01:03:30 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.131 |  |
| 2026-06-13 01:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | 0.067 | 🔺 Rising |
| 2026-06-13 01:03:11 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 01:03:07 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-13 01:03:04 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 01:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.046 |  |
| 2026-06-13 01:02:43 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-06-13 01:02:11 | Ellagawa (Kalu Ganga) | 8.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-13 01:02:08 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.071 |  |
| 2026-06-13 01:02:06 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.107 |  |
| 2026-06-13 01:01:42 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-13 01:01:41 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.346 |  |
| 2026-06-13 01:00:39 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 01:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | 0.067 | 🔺 Rising |
| 2026-06-13 01:05:23 | Magura (Kalu Ganga) | 4.73 | 🟡 Alert | 0.000 |  |
| 2026-06-13 00:05:23 | Rathnapura (Kalu Ganga) | 6.41 | 🟡 Alert | -0.078 |  |
| 2026-06-13 01:04:15 | Pitabeddara (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-13 01:03:47 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-13 01:15:08 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-13 01:03:07 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-13 01:02:11 | Ellagawa (Kalu Ganga) | 8.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-13 01:04:20 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-12 22:06:30 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-13 01:01:42 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-13 01:03:11 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 01:06:20 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-13 01:08:28 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-13 01:03:04 | Dunamale (Aththanagalu Oya) | 3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 01:06:31 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 01:00:39 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:07:08 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:02:14 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:02:50 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:01:11 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:02:44 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-13 01:05:08 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:01:19 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:16:52 | Thawalama (Gin Ganga) | 3.67 | 🟢 Normal | -0.009 |  |
| 2026-06-13 01:05:35 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.010 |  |
| 2026-06-13 01:06:10 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-13 01:02:43 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-06-13 01:09:00 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.019 |  |
| 2026-06-13 01:04:26 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.019 |  |
| 2026-06-13 01:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.046 |  |
| 2026-06-13 01:09:59 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.067 |  |
| 2026-06-13 01:02:08 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.071 |  |
| 2026-06-13 01:02:06 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.107 |  |
| 2026-06-13 01:03:30 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.131 |  |
| 2026-06-13 01:01:41 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.346 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)