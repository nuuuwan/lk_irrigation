# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_04:04:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,163 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 04:04:52 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-01 04:04:37 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:04:30 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:04:19 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:04:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:03:35 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.115 |  |
| 2026-06-01 04:03:28 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.048 |  |
| 2026-06-01 04:02:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:02:44 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-06-01 04:02:42 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:02:39 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-06-01 04:02:38 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:02:35 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:02:17 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:02:01 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.033 |  |
| 2026-06-01 04:01:32 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 04:01:23 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:01:10 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:01:09 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:01:08 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:01:07 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:00:38 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-01 03:41:07 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:25:45 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:13:44 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.048 |  |
| 2026-06-01 03:13:22 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 04:04:52 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-01 04:00:38 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-01 03:07:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-01 03:05:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 04:01:32 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 04:02:42 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:04:37 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:02:35 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:01:08 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:02:55 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:01:09 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 02:41:43 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:06:10 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:01:35 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:02:38 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:13:22 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:04:19 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:01:10 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:01:23 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:03:14 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-01 01:37:18 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:03:58 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:04:30 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:01:07 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:02:17 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 04:04:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:02:01 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 03:03:33 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-01 04:02:44 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-06-01 03:04:53 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-06-01 03:02:21 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-06-01 04:02:39 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-06-01 04:02:01 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.033 |  |
| 2026-06-01 04:03:28 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.048 |  |
| 2026-06-01 03:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | -0.077 |  |
| 2026-06-01 04:03:35 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)