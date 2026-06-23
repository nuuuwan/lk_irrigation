# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_19:08:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,429 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 19:08:01 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.064 |  |
| 2026-06-23 19:07:38 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-06-23 19:06:21 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:05:45 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | -0.120 |  |
| 2026-06-23 19:05:40 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.029 |  |
| 2026-06-23 19:05:38 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-06-23 19:05:20 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | -0.096 |  |
| 2026-06-23 19:05:05 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.019 |  |
| 2026-06-23 19:04:50 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:04:50 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:03:52 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:03:33 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:03:14 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.050 |  |
| 2026-06-23 19:02:46 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:02:37 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | -0.045 |  |
| 2026-06-23 19:02:34 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | -0.020 |  |
| 2026-06-23 19:02:32 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 19:02:21 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-06-23 19:02:20 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-06-23 19:02:18 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:01:54 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-23 19:01:51 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-23 19:01:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:01:21 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:01:17 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:01:17 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-23 19:01:00 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:00:53 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:00:50 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:00:18 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:24:43 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 18:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | -0.022 |  |
| 2026-06-23 19:02:37 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | -0.045 |  |
| 2026-06-23 19:02:20 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-06-23 19:01:54 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-23 19:01:51 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-23 19:02:32 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 19:01:17 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:00:18 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:00:50 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:09:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:02:46 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:06:21 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:01:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:03:33 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:02:18 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:03:52 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:00:53 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:05:56 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:01:21 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:04:50 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:04:50 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-23 19:01:17 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 19:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-23 19:02:21 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-06-23 19:07:38 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-06-23 19:05:05 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.019 |  |
| 2026-06-23 19:02:34 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | -0.020 |  |
| 2026-06-23 19:05:38 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.021 |  |
| 2026-06-23 19:05:40 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.029 |  |
| 2026-06-23 18:02:31 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.041 |  |
| 2026-06-23 19:03:14 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.050 |  |
| 2026-06-23 19:08:01 | Panadugama (Nilwala Ganga) | 3.54 | 🟢 Normal | -0.064 |  |
| 2026-06-23 18:07:12 | Rathnapura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.070 |  |
| 2026-06-23 18:00:34 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.072 |  |
| 2026-06-23 19:05:20 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | -0.096 |  |
| 2026-06-23 19:05:45 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)