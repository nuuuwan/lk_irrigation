# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_22:45:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,751 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 22:45:37 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:13:55 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-21 22:13:16 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-06-21 22:10:45 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.009 |  |
| 2026-06-21 22:10:41 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-21 22:10:30 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-06-21 22:08:33 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.039 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 22:00:55 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-06-21 22:03:07 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-21 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-21 22:13:55 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-21 22:10:41 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-21 22:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 22:02:15 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 22:04:59 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 22:06:23 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 22:04:05 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:01:16 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:01:06 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:03:24 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:01:35 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:02:08 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:45:37 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:51 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:06:18 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:04:35 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:08:09 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:02:18 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:02:22 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:04:34 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:04:32 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:04:38 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:01:38 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 22:10:45 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.009 |  |
| 2026-06-21 22:04:16 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-06-21 21:01:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-21 22:01:34 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-21 22:01:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-21 22:13:16 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-06-21 22:07:05 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-21 22:10:30 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-06-21 22:08:33 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-06-21 22:06:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.066 |  |
| 2026-06-21 22:04:54 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.119 |  |
| 2026-06-21 22:07:26 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)