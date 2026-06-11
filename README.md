# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_02:13:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,960 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 02:13:42 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:12:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-12 02:08:43 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-12 02:07:59 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 02:07:16 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-06-12 02:06:47 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 02:06:45 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 02:06:29 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-12 02:06:11 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-12 02:06:01 | Thawalama (Gin Ganga) | 3.16 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-12 02:05:50 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-06-12 02:05:31 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-12 02:04:59 | Rathnapura (Kalu Ganga) | 5.63 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-06-12 02:04:44 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:04:40 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-12 02:04:37 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-06-12 02:04:33 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.140 |  |
| 2026-06-12 02:04:21 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:04:19 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-06-12 02:03:50 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-12 02:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-06-12 02:03:13 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-06-12 02:03:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:02:43 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:02:27 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-12 02:02:14 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 02:02:10 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:02:01 | Ellagawa (Kalu Ganga) | 7.25 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-06-12 02:01:55 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-06-12 02:01:53 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-06-12 01:53:08 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2026-06-12 01:39:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.038 |  |
| 2026-06-12 01:39:10 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-12 01:29:46 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.139 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 02:04:59 | Rathnapura (Kalu Ganga) | 5.63 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-06-12 02:01:55 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-06-12 02:02:01 | Ellagawa (Kalu Ganga) | 7.25 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-06-12 02:05:50 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-06-12 02:04:19 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-06-12 02:07:16 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-06-12 01:07:38 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-12 02:04:40 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-12 02:06:29 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-12 02:06:01 | Thawalama (Gin Ganga) | 3.16 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-12 02:12:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-12 02:06:11 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-12 02:08:43 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-11 23:11:35 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-12 02:02:27 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-12 02:07:59 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 02:02:14 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-12 02:05:31 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-12 02:03:50 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-12 02:06:45 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 02:06:47 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 02:02:10 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:13:42 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 00:05:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 00:07:13 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:11:49 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:04:44 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-06-12 00:02:42 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:02:43 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:04:21 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:01:15 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:03:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-12 02:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-06-12 02:04:37 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-06-12 02:03:13 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-06-11 18:00:24 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.021 |  |
| 2026-06-12 01:39:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.038 |  |
| 2026-06-12 01:53:08 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2026-06-12 02:04:33 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)