# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_02:15:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,519 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 02:15:51 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:13:54 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:12:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | -0.041 |  |
| 2026-06-16 02:12:08 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:09:13 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.009 |  |
| 2026-06-16 02:08:54 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:07:58 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:07:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:06:22 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:05:55 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 02:04:45 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.264 |  |
| 2026-06-16 02:04:39 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:04:37 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-16 02:04:25 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 02:04:02 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.005 |  |
| 2026-06-16 02:03:55 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:03:15 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:03:04 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-16 02:02:54 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-16 02:02:54 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-16 02:02:41 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-06-16 02:02:25 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.025 |  |
| 2026-06-16 02:02:19 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 02:01:51 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-16 02:01:26 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.020 |  |
| 2026-06-16 02:01:00 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:00:41 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 01:14:43 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-16 01:08:25 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-16 01:39:21 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-16 02:01:51 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-16 02:03:04 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-16 02:04:25 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 02:02:19 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 02:05:55 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 02:04:02 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.005 |  |
| 2026-06-15 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:00:41 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:03:55 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:02:33 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:12:08 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:13:54 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:15:51 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:05:29 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:07:58 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:03:15 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:01:00 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-15 22:04:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:06:22 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:07:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-16 02:04:39 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:27:53 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.008 |  |
| 2026-06-16 02:09:13 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.009 |  |
| 2026-06-16 02:04:37 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:02:56 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-16 02:02:41 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-06-16 02:02:54 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-16 02:02:54 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-16 01:05:56 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-16 02:01:26 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.020 |  |
| 2026-06-15 23:06:09 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-06-16 02:02:25 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.025 |  |
| 2026-06-15 18:00:33 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.026 |  |
| 2026-06-16 02:12:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | -0.041 |  |
| 2026-06-16 02:04:45 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.264 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)