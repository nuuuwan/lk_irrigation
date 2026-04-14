# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_12:00:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,790 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 12:00:45 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:00:41 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:00:32 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 12:00:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:24:37 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.028 |  |
| 2026-04-14 11:20:28 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.018 |  |
| 2026-04-14 11:18:52 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:17:59 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:16:06 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.025 |  |
| 2026-04-14 11:13:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | -0.061 |  |
| 2026-04-14 11:12:16 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.017 |  |
| 2026-04-14 11:11:17 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:10:08 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -0.028 |  |
| 2026-04-14 11:08:39 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:08:24 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:07:48 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:07:22 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 11:04:40 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-14 10:01:40 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-14 11:00:40 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-14 12:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 11:02:55 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 12:00:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:00:45 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:04:47 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:08:39 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:11:17 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:04:36 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:08:24 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:07:48 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:02:19 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:17:59 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:07:22 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:03:24 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:05:01 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-14 10:04:07 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:00:32 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:00:41 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-14 11:12:16 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.017 |  |
| 2026-04-14 11:20:28 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.018 |  |
| 2026-04-14 11:06:49 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-04-14 11:01:54 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-04-14 11:02:38 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.022 |  |
| 2026-04-14 11:16:06 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.025 |  |
| 2026-04-14 11:10:08 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -0.028 |  |
| 2026-04-14 11:24:37 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.028 |  |
| 2026-04-14 11:06:15 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-04-14 11:03:56 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.029 |  |
| 2026-04-14 11:03:13 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.030 |  |
| 2026-04-14 11:02:30 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.040 |  |
| 2026-04-14 11:00:16 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.040 |  |
| 2026-04-14 11:03:30 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.041 |  |
| 2026-04-14 10:00:45 | Kithulgala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.058 |  |
| 2026-04-14 11:13:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | -0.061 |  |
| 2026-04-14 11:03:10 | Thanthirimale (Malwathu Oya) | 4.22 | 🟢 Normal | -0.078 |  |
| 2026-04-14 11:03:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)