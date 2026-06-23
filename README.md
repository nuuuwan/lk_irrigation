# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_00:22:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,616 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 00:22:14 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.039 |  |
| 2026-06-24 00:20:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.006 |  |
| 2026-06-24 00:18:49 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:11:59 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-06-24 00:08:40 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.027 |  |
| 2026-06-24 00:08:03 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:07:42 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-06-24 00:07:04 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-24 00:06:47 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | -0.020 |  |
| 2026-06-24 00:06:07 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 59.470 | 🔺 Rising |
| 2026-06-24 00:06:05 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:05:50 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.211 |  |
| 2026-06-24 00:05:41 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | -0.085 |  |
| 2026-06-24 00:05:36 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:05:20 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:05:04 | Ellagawa (Kalu Ganga) | 7.73 | 🟢 Normal | -0.020 |  |
| 2026-06-24 00:04:31 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-06-24 00:04:28 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.026 |  |
| 2026-06-24 00:04:16 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:03:47 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:03:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.046 |  |
| 2026-06-24 00:03:06 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 59.470 | 🔺 Rising |
| 2026-06-24 00:03:06 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-06-24 00:02:53 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:02:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:02:51 | Dunamale (Aththanagalu Oya) | 3.60 | 🟡 Alert | -0.050 |  |
| 2026-06-24 00:02:25 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.020 |  |
| 2026-06-24 00:02:23 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:02:23 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:02:01 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:01:49 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-24 00:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-24 00:01:38 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:01:28 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:01:14 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.076 |  |
| 2026-06-24 00:01:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:00:10 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:48:45 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.211 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 00:20:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.006 |  |
| 2026-06-24 00:02:51 | Dunamale (Aththanagalu Oya) | 3.60 | 🟡 Alert | -0.050 |  |
| 2026-06-24 00:06:07 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 59.470 | 🔺 Rising |
| 2026-06-24 00:07:42 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-06-24 00:03:47 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:02:23 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:01:01 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:02:23 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:02:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:00:10 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:06:05 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:02:53 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:02:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:01:38 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:05:20 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:08:03 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:05:36 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:18:49 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:02:01 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:01:28 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:07:04 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-24 00:04:31 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-06-24 00:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-24 00:01:49 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-24 00:11:59 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-06-24 00:05:04 | Ellagawa (Kalu Ganga) | 7.73 | 🟢 Normal | -0.020 |  |
| 2026-06-24 00:06:47 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | -0.020 |  |
| 2026-06-24 00:02:25 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.020 |  |
| 2026-06-24 00:04:28 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.026 |  |
| 2026-06-24 00:08:40 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.027 |  |
| 2026-06-24 00:22:14 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.039 |  |
| 2026-06-24 00:03:06 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-06-24 00:03:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.046 |  |
| 2026-06-24 00:01:14 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.076 |  |
| 2026-06-24 00:05:41 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | -0.085 |  |
| 2026-06-24 00:05:50 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.211 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)