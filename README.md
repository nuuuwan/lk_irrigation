# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_13:10:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,046 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 13:10:18 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:09:25 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-04 13:08:02 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.067 |  |
| 2026-07-04 13:07:43 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 13:07:21 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:05:27 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-07-04 13:05:16 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-07-04 13:05:00 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-07-04 13:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.089 |  |
| 2026-07-04 13:03:50 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 13:03:37 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-07-04 13:03:25 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-04 13:03:19 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.062 |  |
| 2026-07-04 13:03:17 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 13:03:13 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.191 |  |
| 2026-07-04 13:03:11 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-07-04 13:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:03:04 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:02:45 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:02:33 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:02:24 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:02:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:02:08 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 13:02:06 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-07-04 13:01:55 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:01:46 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-04 13:01:46 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-07-04 13:01:40 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-04 13:01:31 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:01:11 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-07-04 13:01:01 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.041 |  |
| 2026-07-04 13:00:36 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:00:26 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:00:20 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 13:05:00 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-07-04 13:05:16 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-07-04 13:01:46 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-07-04 13:03:37 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-07-04 13:03:11 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-07-04 13:09:25 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-04 13:02:06 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-07-04 13:03:25 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-04 13:03:50 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 13:02:08 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 13:03:17 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 13:07:43 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 13:00:26 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:02:24 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:01:55 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:02:33 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:07:21 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:03 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:10:18 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:01:32 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:02:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:01:31 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:03:04 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:00:36 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:04:32 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 12:06:22 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:02:45 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-07-04 13:01:46 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-07-04 13:01:40 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-04 13:00:20 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-07-04 12:12:57 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.019 |  |
| 2026-07-04 13:05:27 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-07-04 13:01:11 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-07-04 13:01:01 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.041 |  |
| 2026-07-04 13:03:19 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.062 |  |
| 2026-07-04 13:08:02 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.067 |  |
| 2026-07-04 13:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.089 |  |
| 2026-07-04 13:03:13 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)