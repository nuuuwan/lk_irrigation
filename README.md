# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_21:00:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,533 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 21:00:13 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-13 20:27:58 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.029 |  |
| 2026-03-13 20:09:16 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:08:46 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 20:08:38 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:08:17 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:06:21 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 20:03:47 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-03-13 20:04:49 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-13 20:01:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-13 20:02:06 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-13 20:04:55 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-13 20:03:47 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-13 20:04:47 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 20:03:22 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 20:02:25 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 20:03:03 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 20:08:46 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 20:00:49 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:09:16 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:01:51 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:03:11 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:04:31 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:03:44 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:08:17 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:02:15 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:02:52 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:02:53 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:04:55 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:05:09 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:02:36 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:08:38 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-13 20:03:01 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-13 21:00:13 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-13 20:02:43 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-03-13 20:04:29 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-03-13 20:01:04 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-03-13 20:27:58 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.029 |  |
| 2026-03-13 20:06:21 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.041 |  |
| 2026-03-13 20:05:12 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.048 |  |
| 2026-03-13 20:04:30 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.061 |  |
| 2026-03-13 20:05:04 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.069 |  |
| 2026-03-13 20:05:28 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.071 |  |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)