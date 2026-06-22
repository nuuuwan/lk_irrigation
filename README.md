# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_04:35:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,850 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 04:35:17 | Rathnapura (Kalu Ganga) | 4.02 | 🟢 Normal | -0.016 |  |
| 2026-06-23 04:33:45 | Deraniyagala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-23 04:14:29 | Holombuwa (Kelani Ganga) | 1.55 | 🟢 Normal | -0.258 |  |
| 2026-06-23 04:11:51 | Thawalama (Gin Ganga) | 3.12 | 🟢 Normal | -0.119 |  |
| 2026-06-23 04:08:52 | Magura (Kalu Ganga) | 4.00 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-06-23 04:08:19 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-06-23 04:07:40 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.018 |  |
| 2026-06-23 04:06:51 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 04:02:58 | Dunamale (Aththanagalu Oya) | 3.87 | 🟡 Alert | 0.071 | 🔺 Rising |
| 2026-06-23 04:00:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.77 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-06-23 04:08:52 | Magura (Kalu Ganga) | 4.00 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-06-23 04:04:13 | Hanwella (Kelani Ganga) | 4.88 | 🟢 Normal | 0.407 | 🔺 Rising |
| 2026-06-23 04:08:19 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-06-23 04:33:45 | Deraniyagala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-23 04:04:35 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-23 04:05:33 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-23 03:21:34 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-23 04:05:07 | Giriulla (Maha Oya) | 2.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-23 04:02:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 04:01:39 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-23 04:03:41 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-23 04:06:35 | Putupaula (Kalu Ganga) | 2.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 03:00:55 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 04:03:53 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:01:02 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-23 01:01:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 04:01:37 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:23 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:11:05 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-23 04:00:25 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 04:02:01 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 04:05:19 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 18:03:55 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:05:17 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-06-23 04:01:20 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 04:01:25 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-23 03:06:02 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-06-23 04:35:17 | Rathnapura (Kalu Ganga) | 4.02 | 🟢 Normal | -0.016 |  |
| 2026-06-23 04:06:51 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.016 |  |
| 2026-06-23 04:07:40 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.018 |  |
| 2026-06-23 04:03:20 | Glencourse (Kelani Ganga) | 13.38 | 🟢 Normal | -0.021 |  |
| 2026-06-23 04:03:12 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.022 |  |
| 2026-06-22 18:01:33 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.029 |  |
| 2026-06-23 04:02:04 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.107 |  |
| 2026-06-23 04:11:51 | Thawalama (Gin Ganga) | 3.12 | 🟢 Normal | -0.119 |  |
| 2026-06-23 04:14:29 | Holombuwa (Kelani Ganga) | 1.55 | 🟢 Normal | -0.258 |  |
| 2026-06-23 04:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.659 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)