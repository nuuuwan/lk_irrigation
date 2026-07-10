# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_04:04:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **202,989 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 04:04:37 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:04:32 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.063 |  |
| 2026-07-11 04:04:02 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:04:00 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:03:39 | Peradeniya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.070 |  |
| 2026-07-11 04:03:39 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:03:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:03:16 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:02:30 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:02:27 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-11 04:02:19 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:15 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:15 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-11 04:02:11 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:01 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:01:44 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 04:01:37 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:01:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:01:09 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-11 03:58:00 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 03:22:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.017 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 03:02:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-11 04:02:15 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-11 04:01:09 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-11 04:01:44 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 03:22:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-11 04:02:27 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-11 04:03:16 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:04:00 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:02:30 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:03:39 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 01:03:53 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.005 |  |
| 2026-07-10 18:05:00 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:11 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:15 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:01 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 03:04:41 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:09:34 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:17:40 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 03:03:01 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:04:37 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:03:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:00:36 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:01:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:19 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 03:02:18 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:40 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-11 03:09:11 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:04:02 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 03:02:54 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:01:37 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 03:15:00 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-07-11 02:38:03 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.013 |  |
| 2026-07-11 03:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-07-11 01:10:00 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.028 |  |
| 2026-07-11 03:04:47 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-07-11 04:04:32 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.063 |  |
| 2026-07-11 04:03:39 | Peradeniya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.070 |  |
| 2026-07-11 03:04:12 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.408 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)