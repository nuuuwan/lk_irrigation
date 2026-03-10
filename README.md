# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_05:24:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,046 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 05:24:58 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-03-10 05:23:07 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | -0.007 |  |
| 2026-03-10 05:12:11 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:11:13 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:10:15 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:08:04 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:07:55 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-03-10 05:07:28 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:07:14 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-10 05:06:11 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-10 05:05:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:05:14 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:05:14 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-03-10 05:04:38 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-10 05:04:24 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-03-10 05:03:51 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:03:41 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-03-10 05:03:14 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-10 05:03:14 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.027 |  |
| 2026-03-10 05:02:53 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 05:02:47 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:02:41 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:02:39 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:02:37 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:02:29 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:02:14 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:02:14 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-03-10 05:01:45 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:01:12 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.011 |  |
| 2026-03-10 05:01:07 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:01:06 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:00:36 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.101 |  |
| 2026-03-10 05:00:27 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | -0.092 |  |
| 2026-03-10 05:00:16 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:45:22 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 18:01:06 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-10 05:06:11 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-09 22:02:21 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-10 05:04:38 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-10 05:02:53 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 05:02:37 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:01:07 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:05:14 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:02:47 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:02:29 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:01:06 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-09 18:06:39 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:08:04 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:03:14 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:10:15 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-10 03:00:22 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:00:16 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:01:45 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:05:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:07:28 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 04:01:49 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:03:51 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:12:11 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:02:39 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:11:13 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:23:07 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | -0.007 |  |
| 2026-03-10 05:07:55 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-03-10 05:04:24 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-03-10 05:03:14 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-10 05:07:14 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-10 05:01:12 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.011 |  |
| 2026-03-10 05:05:14 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-03-10 05:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.027 |  |
| 2026-03-10 05:24:58 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-03-10 05:02:14 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-03-10 05:03:41 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-03-09 18:01:53 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.075 |  |
| 2026-03-10 05:00:27 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | -0.092 |  |
| 2026-03-10 05:00:36 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)