# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_13:08:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,933 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 13:08:06 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:07:57 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-16 13:07:49 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2026-06-16 13:07:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-16 13:07:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:07:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:07:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.155 |  |
| 2026-06-16 13:05:27 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:05:17 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:05:11 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:05:04 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:04:51 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.049 |  |
| 2026-06-16 13:04:47 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-16 13:04:33 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-16 13:04:30 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-06-16 13:04:22 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-06-16 13:04:03 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:04:02 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:03:58 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:03:49 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:03:47 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:03:35 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:03:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-06-16 13:03:06 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:03:04 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:02:58 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-06-16 13:02:37 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:02:33 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.081 |  |
| 2026-06-16 13:02:11 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:02:07 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:01:12 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.110 |  |
| 2026-06-16 13:01:02 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:00:52 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:00:37 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 13:03:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-06-16 13:04:47 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-16 13:07:57 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-16 13:07:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-16 13:04:33 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-16 13:00:52 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:05:04 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 12:06:08 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:03:58 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:05:27 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:00:37 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:07:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:04:03 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:05:11 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:03:35 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:03:06 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-16 12:03:39 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:03:47 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:02:37 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:02:11 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:02:07 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 13:04:30 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-06-16 13:08:06 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:03:49 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:05:17 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:07:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:01:02 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:04:02 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:03:04 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-06-16 13:02:58 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-06-16 12:03:30 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-06-16 13:07:49 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2026-06-16 13:04:22 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-06-16 12:09:40 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2026-06-16 13:04:51 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.049 |  |
| 2026-06-16 13:02:33 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.081 |  |
| 2026-06-16 13:01:12 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.110 |  |
| 2026-06-16 13:07:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)