# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_12:39:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,129 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 12:39:18 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-14 12:12:00 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.064 |  |
| 2026-06-14 12:11:02 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.061 |  |
| 2026-06-14 12:10:59 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-06-14 12:08:44 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.058 |  |
| 2026-06-14 12:08:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-06-14 12:08:21 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 12:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | -0.030 |  |
| 2026-06-14 12:03:36 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-06-14 12:04:39 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-14 12:00:33 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-14 12:39:18 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-14 12:06:25 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 12:01:24 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.003 |  |
| 2026-06-14 12:01:21 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-14 12:02:12 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-14 12:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-14 12:01:15 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 12:04:53 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-14 12:06:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 12:00:13 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-14 12:02:38 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-14 12:01:14 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 12:07:37 | Rathnapura (Kalu Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-14 12:04:28 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-14 12:10:59 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-06-14 12:08:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-06-14 12:05:57 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-06-14 12:02:41 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-06-14 12:01:11 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-14 12:01:35 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-06-14 12:07:19 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-06-14 12:05:28 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.021 |  |
| 2026-06-14 12:04:01 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.022 |  |
| 2026-06-14 12:05:50 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | -0.024 |  |
| 2026-06-14 12:02:47 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-06-14 12:00:43 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.030 |  |
| 2026-06-14 12:02:28 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | -0.041 |  |
| 2026-06-14 12:04:53 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.049 |  |
| 2026-06-14 12:08:21 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.050 |  |
| 2026-06-14 12:03:00 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.051 |  |
| 2026-06-14 12:08:44 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.058 |  |
| 2026-06-14 12:01:55 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | -0.061 |  |
| 2026-06-14 12:11:02 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.061 |  |
| 2026-06-14 12:12:00 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.064 |  |
| 2026-06-14 12:04:59 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)