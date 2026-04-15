# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_00:24:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,166 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 00:24:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 2.700 | 🔺 Rising |
| 2026-04-16 00:23:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 2.700 | 🔺 Rising |
| 2026-04-16 00:20:24 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:12:51 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-04-16 00:11:20 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:09:08 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-16 00:07:13 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.029 |  |
| 2026-04-16 00:06:50 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:06:19 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-04-16 00:05:44 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:05:34 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:05:22 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 00:24:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 2.700 | 🔺 Rising |
| 2026-04-16 00:02:33 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-04-16 00:01:18 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-16 00:03:09 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-16 00:09:08 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-16 00:04:23 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-16 00:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-15 22:13:02 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-15 22:00:58 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 00:11:20 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:02:55 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:01:20 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:20:24 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:01:38 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:01:48 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:06:50 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:02:26 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:05:22 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:01:09 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:03:22 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:01:15 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:01:34 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:05:44 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:05:34 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:02:15 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:04:42 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-16 00:12:51 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-04-16 00:04:35 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-04-16 00:06:19 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-04-16 00:03:47 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-16 00:04:40 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.012 |  |
| 2026-04-16 00:03:06 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.020 |  |
| 2026-04-16 00:02:30 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.022 |  |
| 2026-04-16 00:07:13 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.029 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |
| 2026-04-16 00:04:01 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.132 |  |
| 2026-04-16 00:00:12 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.240 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)