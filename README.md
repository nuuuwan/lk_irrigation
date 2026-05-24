# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_02:02:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,828 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 02:02:42 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:02:34 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:02:31 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.080 |  |
| 2026-05-25 02:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-25 02:01:49 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:01:43 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:01:29 | Ellagawa (Kalu Ganga) | 9.29 | 🟢 Normal | -0.050 |  |
| 2026-05-25 02:01:22 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:00:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 02:00:44 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:00:43 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-05-25 02:00:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 01:05:49 | Putupaula (Kalu Ganga) | 3.24 | 🟡 Alert | 0.000 |  |
| 2026-05-25 00:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | -0.010 |  |
| 2026-05-25 01:01:39 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.866 | 🔺 Rising |
| 2026-05-25 01:03:38 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-05-25 01:03:29 | Hanwella (Kelani Ganga) | 4.24 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-05-25 02:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-25 01:02:59 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-25 01:01:27 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 01:01:56 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 01:02:25 | Nagalagam Street (Kelani Ganga) | 0.81 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-25 02:00:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 01:06:39 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:57 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:00:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:01:22 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:02:34 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:01:56 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:01:43 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:50 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 01:01:44 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-25 01:03:07 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:02:42 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 01:02:33 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:05:55 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-25 01:04:22 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:01:49 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 01:03:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-25 00:17:39 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-25 01:01:30 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-25 01:02:12 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-25 01:05:10 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-05-25 01:05:56 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-05-25 02:00:43 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-05-25 02:01:29 | Ellagawa (Kalu Ganga) | 9.29 | 🟢 Normal | -0.050 |  |
| 2026-05-25 02:02:31 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.080 |  |
| 2026-05-25 01:02:01 | Rathnapura (Kalu Ganga) | 5.15 | 🟢 Normal | -0.080 |  |
| 2026-05-25 01:10:21 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.189 |  |
| 2026-05-25 01:02:53 | Deraniyagala (Kelani Ganga) | 2.34 | 🟢 Normal | -0.262 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)