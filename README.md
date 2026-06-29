# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_06:29:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,298 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 06:29:06 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.001 |  |
| 2026-06-29 06:18:43 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:13:02 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:12:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.008 |  |
| 2026-06-29 06:12:02 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-06-29 06:11:51 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:09:02 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-29 06:07:59 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-29 06:07:51 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-06-29 06:07:45 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:07:33 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | -0.010 |  |
| 2026-06-29 06:07:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 9.578 | 🔺 Rising |
| 2026-06-29 06:06:50 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-29 06:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.25 | 🟢 Normal | 9.578 | 🔺 Rising |
| 2026-06-29 06:05:37 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:05:29 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-29 06:05:08 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-06-29 06:05:04 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:04:55 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-06-29 06:04:47 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.076 |  |
| 2026-06-29 06:04:34 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 06:04:25 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-06-29 06:03:56 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:03:49 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:03:19 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-29 06:03:10 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:03:07 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 06:07:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 9.578 | 🔺 Rising |
| 2026-06-29 06:00:50 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-06-29 06:12:02 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-06-29 06:06:50 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-29 06:05:29 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-29 06:07:51 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-06-29 06:03:19 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-29 06:07:59 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-29 06:02:23 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-29 06:01:23 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 06:00:48 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-29 06:09:02 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-29 06:04:34 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 06:02:00 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:02:33 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:03:56 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:03:07 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:02:07 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:03:10 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:13:02 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:18:43 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:02:36 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:03:49 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:05:37 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:05:04 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:07:45 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:01:12 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:02:20 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 06:29:06 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.001 |  |
| 2026-06-29 06:12:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.008 |  |
| 2026-06-28 18:01:23 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-06-29 06:07:33 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | -0.010 |  |
| 2026-06-29 06:05:08 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-06-29 06:04:25 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-06-29 06:04:55 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-06-29 06:00:42 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | -0.061 |  |
| 2026-06-29 06:04:47 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.076 |  |
| 2026-06-29 06:00:53 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)