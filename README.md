# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_04:19:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,588 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 04:19:49 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:18:53 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.016 |  |
| 2026-06-16 04:08:45 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-16 04:08:40 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-16 04:08:17 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:07:57 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:07:04 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:07:02 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:06:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 04:05:17 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.020 |  |
| 2026-06-16 04:04:09 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-16 04:03:54 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-16 04:03:52 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:03:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.098 |  |
| 2026-06-16 04:03:35 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:03:33 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-16 04:03:24 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:03:11 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:03:01 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-16 04:02:51 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:02:48 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-06-16 04:02:46 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 04:02:31 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.197 |  |
| 2026-06-16 04:01:47 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-06-16 04:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:01:33 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:01:17 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.010 |  |
| 2026-06-16 04:00:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 04:00:43 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 04:08:45 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-16 04:08:40 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-16 03:03:04 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-16 04:04:09 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-16 04:03:54 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-16 04:03:33 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-16 04:00:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 04:06:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 04:02:46 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 04:02:51 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.000 |  |
| 2026-06-16 03:00:47 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:03:35 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:03:11 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:01:33 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-16 03:05:16 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:08:17 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:07:04 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:03:52 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:03:24 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:07:02 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:07:57 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:07:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-16 03:02:10 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-16 04:19:49 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 18:02:56 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-16 04:03:01 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-16 04:00:43 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-16 04:01:17 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.010 |  |
| 2026-06-16 04:01:47 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-06-16 02:56:32 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.016 |  |
| 2026-06-16 04:18:53 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.016 |  |
| 2026-06-16 04:05:17 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.020 |  |
| 2026-06-15 18:00:33 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.026 |  |
| 2026-06-16 04:02:48 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-06-16 02:12:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | -0.041 |  |
| 2026-06-16 04:03:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.098 |  |
| 2026-06-16 04:02:31 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)