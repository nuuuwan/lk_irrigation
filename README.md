# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_04:21:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,419 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 04:21:45 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-22 04:18:36 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:16:17 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-05-22 04:15:37 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-22 04:13:13 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.018 |  |
| 2026-05-22 04:12:26 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.012 |  |
| 2026-05-22 04:12:24 | Badalgama (Maha Oya) | 3.90 | 🟢 Normal | 0.561 | 🔺 Rising |
| 2026-05-22 04:11:58 | Glencourse (Kelani Ganga) | 12.56 | 🟢 Normal | 0.723 | 🔺 Rising |
| 2026-05-22 04:11:11 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-22 04:10:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-22 04:07:38 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | 0.921 | 🔺 Rising |
| 2026-05-22 04:06:43 | Rathnapura (Kalu Ganga) | 4.74 | 🟢 Normal | 1.835 | 🔺 Rising |
| 2026-05-22 04:06:42 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-22 04:06:15 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-22 04:06:01 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:05:54 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-22 04:05:06 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-22 04:05:05 | Deraniyagala (Kelani Ganga) | 3.54 | 🟢 Normal | 1.378 | 🔺 Rising |
| 2026-05-22 04:04:41 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-05-22 04:04:29 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | 0.557 | 🔺 Rising |
| 2026-05-22 04:04:22 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 04:03:33 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 04:02:33 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-05-22 04:02:16 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-05-22 04:02:15 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-05-22 04:02:12 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:02:09 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-05-22 04:01:50 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:01:49 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-05-22 04:01:34 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:01:19 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.072 |  |
| 2026-05-22 04:01:16 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-22 04:01:10 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:40:53 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | 1.835 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 04:02:16 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-05-22 04:06:43 | Rathnapura (Kalu Ganga) | 4.74 | 🟢 Normal | 1.835 | 🔺 Rising |
| 2026-05-22 04:05:05 | Deraniyagala (Kelani Ganga) | 3.54 | 🟢 Normal | 1.378 | 🔺 Rising |
| 2026-05-22 04:07:38 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | 0.921 | 🔺 Rising |
| 2026-05-22 04:11:58 | Glencourse (Kelani Ganga) | 12.56 | 🟢 Normal | 0.723 | 🔺 Rising |
| 2026-05-22 04:04:41 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-05-22 04:12:24 | Badalgama (Maha Oya) | 3.90 | 🟢 Normal | 0.561 | 🔺 Rising |
| 2026-05-22 04:04:29 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | 0.557 | 🔺 Rising |
| 2026-05-22 04:02:33 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-05-22 04:16:17 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-05-22 04:05:06 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-22 04:06:42 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-22 04:11:11 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-22 04:15:37 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-22 04:06:15 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-22 04:10:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-22 03:30:54 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-22 04:05:54 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-22 04:03:33 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 04:04:22 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 18:16:06 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-22 04:21:45 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-22 04:02:12 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:01:34 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:06:01 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:02:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:27 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:24:00 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:01:10 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:01:50 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:18:36 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:02:24 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-22 04:01:16 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-22 04:12:26 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.012 |  |
| 2026-05-22 04:13:13 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.018 |  |
| 2026-05-22 03:04:47 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-05-22 04:02:09 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-22 04:01:19 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)