# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_12:01:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,020 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 12:01:34 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:01:19 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 12:01:18 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-04-21 12:01:07 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-04-21 12:01:02 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:00:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-21 12:00:11 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.040 |  |
| 2026-04-21 12:00:09 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-21 11:09:42 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-04-21 11:08:48 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 11:05:50 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-04-21 11:03:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-21 12:00:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-21 11:06:36 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-21 11:01:39 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-21 11:06:01 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-21 11:01:17 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-21 12:01:19 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 11:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 11:02:35 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 12:01:02 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:01:34 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:01:18 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-21 11:05:04 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 11:01:32 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 11:01:35 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 11:02:13 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 11:04:27 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 11:03:43 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-21 11:06:32 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-21 11:08:48 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-04-21 11:03:10 | Galgamuwa (Mee Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-21 11:04:31 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2026-04-21 11:03:06 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-04-21 11:09:42 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-04-21 12:01:07 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-04-21 11:05:39 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-04-21 12:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-04-21 11:07:12 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.021 |  |
| 2026-04-21 11:06:36 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.040 |  |
| 2026-04-21 12:00:11 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.040 |  |
| 2026-04-21 11:04:01 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.040 |  |
| 2026-04-21 11:03:11 | Hanwella (Kelani Ganga) | 1.91 | 🟢 Normal | -0.050 |  |
| 2026-04-21 11:01:35 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.061 |  |
| 2026-04-21 11:04:23 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.066 |  |
| 2026-04-21 11:01:22 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.091 |  |
| 2026-04-21 11:08:14 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.139 |  |
| 2026-04-21 11:02:06 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.141 |  |
| 2026-04-21 11:01:12 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)