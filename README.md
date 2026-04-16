# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_01:28:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,088 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 01:28:17 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:23:49 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-17 01:12:15 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-17 01:07:49 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:06:31 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 01:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-17 01:23:49 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-17 01:04:03 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-17 00:03:39 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-17 01:06:11 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 01:03:17 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 01:00:50 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 01:01:00 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 00:04:06 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 01:04:55 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 01:02:28 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 01:07:49 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:01:02 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:01:48 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:03:08 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:19 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:05:33 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:06:21 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:04:45 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:01:46 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:28:17 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:03:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:03:51 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:02:38 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:06:31 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:12:15 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-17 01:05:53 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-17 01:02:48 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.014 |  |
| 2026-04-17 00:22:45 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.017 |  |
| 2026-04-17 01:05:17 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-04-17 01:06:17 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-04-17 01:01:37 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -0.020 |  |
| 2026-04-17 00:01:47 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-04-17 01:01:10 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.032 |  |
| 2026-04-17 00:02:19 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-04-17 01:03:08 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.359 |  |
| 2026-04-16 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -4.696 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)