# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_16:18:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,364 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 16:18:28 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:17:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.032 |  |
| 2026-06-04 16:16:42 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.008 |  |
| 2026-06-04 16:13:41 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:10:23 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:08:58 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 16:07:45 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:06:37 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:06:10 | Hanwella (Kelani Ganga) | 2.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 16:05:53 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 16:05:49 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:05:03 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-06-04 16:04:58 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:04:52 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.190 |  |
| 2026-06-04 16:04:50 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-04 16:04:19 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.050 |  |
| 2026-06-04 16:04:00 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-04 16:03:57 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 16:03:47 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-04 16:03:39 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:03:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.041 |  |
| 2026-06-04 16:03:17 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 16:03:08 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 16:02:48 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 16:02:43 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-06-04 16:02:41 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 16:02:25 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 16:02:23 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:01:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:01:27 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 16:01:20 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-04 16:01:19 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:01:09 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:00:49 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-06-04 16:00:48 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:00:12 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:00:09 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 16:04:00 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-04 16:04:50 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-04 16:01:20 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-04 16:03:17 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 16:03:47 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-04 16:06:10 | Hanwella (Kelani Ganga) | 2.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 16:02:25 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 16:03:57 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 16:03:08 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 16:01:27 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 16:02:41 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 16:02:48 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 16:05:53 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 16:08:58 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 16:00:12 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:00:48 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:00:09 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:01:19 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:10:23 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:01:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:07:45 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:06:37 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-04 15:09:29 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:05:49 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:18:28 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:01:09 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:03:39 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:02:23 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:04:58 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:13:41 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-04 16:16:42 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.008 |  |
| 2026-06-04 15:03:46 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-04 16:05:03 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-06-04 16:00:49 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-06-04 16:02:43 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-06-04 16:17:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.032 |  |
| 2026-06-04 16:03:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.041 |  |
| 2026-06-04 16:04:19 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.050 |  |
| 2026-06-04 16:04:52 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.190 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)