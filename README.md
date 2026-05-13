# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_20:48:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 20:48:39 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 20:15:37 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.008 |  |
| 2026-05-13 20:10:35 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.028 |  |
| 2026-05-13 20:09:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.86 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-05-13 20:07:42 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.037 |  |
| 2026-05-13 20:07:33 | Thanamalwila (Kirindi Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-13 20:07:14 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.055 |  |
| 2026-05-13 20:06:41 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 20:06:22 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-05-13 20:05:53 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | -0.078 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 20:09:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.86 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-05-13 20:02:20 | Dunamale (Aththanagalu Oya) | 3.50 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-13 20:02:47 | Magura (Kalu Ganga) | 5.17 | 🟡 Alert | 0.000 |  |
| 2026-05-13 20:05:53 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | -0.078 |  |
| 2026-05-13 20:03:23 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | -0.085 |  |
| 2026-05-13 20:04:29 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-13 20:01:58 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-13 20:02:43 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-13 20:03:37 | Ellagawa (Kalu Ganga) | 8.05 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-13 20:04:30 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-13 20:02:51 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 20:01:05 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 20:04:59 | Putupaula (Kalu Ganga) | 2.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 20:01:47 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 20:01:35 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 20:02:36 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-13 20:48:39 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 20:06:41 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 20:07:33 | Thanamalwila (Kirindi Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-13 20:15:37 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.008 |  |
| 2026-05-13 20:03:46 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-13 20:03:25 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-05-13 20:04:18 | Moragaswewa (Deduru Oya) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-05-13 20:02:29 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-13 20:06:22 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-05-13 20:01:33 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-05-13 20:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-05-13 20:10:35 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.028 |  |
| 2026-05-13 20:07:42 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.037 |  |
| 2026-05-13 20:04:31 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-05-13 20:03:34 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.039 |  |
| 2026-05-13 20:02:38 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.040 |  |
| 2026-05-13 20:00:46 | Moraketiya (Walawe Ganga) | 2.07 | 🟢 Normal | -0.048 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-13 20:07:14 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.055 |  |
| 2026-05-13 20:03:35 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.079 |  |
| 2026-05-13 20:04:12 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)