# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_02:28:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,855 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 02:28:59 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-13 02:13:39 | Thawalama (Gin Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:10:45 | Rathnapura (Kalu Ganga) | 6.31 | 🟡 Alert | -0.048 |  |
| 2026-06-13 02:09:30 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-06-13 02:08:57 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-06-13 02:08:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-06-13 02:07:52 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-13 02:07:50 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.019 |  |
| 2026-06-13 02:07:43 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-06-13 02:06:50 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-13 02:06:47 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-13 02:06:15 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 02:05:52 | Glencourse (Kelani Ganga) | 12.25 | 🟢 Normal | -0.053 |  |
| 2026-06-13 02:05:36 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:05:25 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:03:34 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.010 |  |
| 2026-06-13 02:03:23 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.039 |  |
| 2026-06-13 02:03:14 | Urawa (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.151 |  |
| 2026-06-13 02:02:57 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-06-13 02:02:55 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 02:02:52 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:02:45 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 02:02:20 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 02:02:11 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:02:05 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.005 |  |
| 2026-06-13 02:02:00 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 02:01:37 | Ellagawa (Kalu Ganga) | 8.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 02:01:29 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.211 |  |
| 2026-06-13 02:01:25 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:00:38 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:00:23 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-13 01:59:03 | Thawalama (Gin Ganga) | 3.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 02:08:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-06-13 02:03:34 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.010 |  |
| 2026-06-13 02:10:45 | Rathnapura (Kalu Ganga) | 6.31 | 🟡 Alert | -0.048 |  |
| 2026-06-13 02:09:30 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-06-13 02:07:43 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-06-13 02:06:47 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-13 02:07:52 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-13 02:02:45 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 02:02:55 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 02:06:50 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-13 02:02:20 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 02:06:15 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 02:02:00 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-13 02:01:37 | Ellagawa (Kalu Ganga) | 8.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 01:20:20 | Putupaula (Kalu Ganga) | 2.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-13 02:28:59 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:00:23 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:07:08 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:05:36 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-12 23:02:14 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:00:38 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:01:25 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:02:11 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:02:52 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:13:39 | Thawalama (Gin Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-06-13 00:01:19 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:05:25 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-13 02:02:05 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.005 |  |
| 2026-06-13 02:02:57 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-06-13 02:07:50 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.019 |  |
| 2026-06-13 02:08:57 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-06-13 02:03:23 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.039 |  |
| 2026-06-13 01:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.046 |  |
| 2026-06-13 02:05:52 | Glencourse (Kelani Ganga) | 12.25 | 🟢 Normal | -0.053 |  |
| 2026-06-13 02:03:14 | Urawa (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.151 |  |
| 2026-06-13 02:01:29 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.211 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)