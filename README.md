# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_14:18:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,089 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 14:18:36 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 14:17:09 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-27 14:15:20 | Magura (Kalu Ganga) | 3.15 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-27 14:08:18 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:08:14 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-27 14:07:15 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.040 |  |
| 2026-05-27 14:06:17 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-05-27 14:05:58 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -36.000 |  |
| 2026-05-27 14:05:57 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -36.000 |  |
| 2026-05-27 14:05:55 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 14:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-27 14:02:05 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-05-27 14:03:44 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-27 14:01:23 | Glencourse (Kelani Ganga) | 11.83 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-27 14:01:06 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-27 14:15:20 | Magura (Kalu Ganga) | 3.15 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-27 14:03:20 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-27 14:01:52 | Dunamale (Aththanagalu Oya) | 2.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-27 14:17:09 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-27 14:08:14 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-27 14:04:21 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 14:03:36 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 14:18:36 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 14:00:49 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:00:58 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:03:44 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:01:00 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:01:35 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:02:39 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:00:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:04:12 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:02:47 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:01:47 | Ellagawa (Kalu Ganga) | 8.44 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:02:16 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:01:13 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:00:47 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:01:09 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:03:21 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:01:14 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:08:18 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:01:47 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 14:06:17 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-05-27 14:00:33 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-05-27 14:01:11 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | -0.040 |  |
| 2026-05-27 14:07:15 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.040 |  |
| 2026-05-27 14:02:58 | Deraniyagala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.051 |  |
| 2026-05-27 14:05:55 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.062 |  |
| 2026-05-27 14:05:58 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)