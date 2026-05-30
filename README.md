# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_13:01:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,698 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **4** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 13:01:00 | Ellagawa (Kalu Ganga) | 7.67 | 🟢 Normal | -0.087 |  |
| 2026-05-30 13:00:59 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:00:08 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.022 |  |
| 2026-05-30 12:18:29 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 12:09:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.41 | 🟡 Alert | -0.027 |  |
| 2026-05-30 12:04:01 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 4.000 | 🔺 Rising |
| 2026-05-30 12:13:11 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-30 12:04:24 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-30 12:05:06 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-30 11:02:07 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:03:16 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:02:00 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:03:15 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:01:14 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:18:29 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:03:53 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:02:20 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:03:08 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:02:19 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:05:11 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:06:06 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-30 13:00:59 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:05:22 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:05:56 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:02:40 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 12:03:47 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-05-30 12:03:54 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-05-30 12:04:38 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-30 12:03:02 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-05-30 12:00:40 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-30 12:01:13 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.014 |  |
| 2026-05-30 12:05:33 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.019 |  |
| 2026-05-30 13:00:08 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.022 |  |
| 2026-05-30 12:09:54 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | -0.028 |  |
| 2026-05-30 12:04:07 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-05-30 12:02:38 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | -0.033 |  |
| 2026-05-30 12:02:10 | Baddegama (Gin Ganga) | 2.87 | 🟢 Normal | -0.033 |  |
| 2026-05-30 12:01:37 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.036 |  |
| 2026-05-30 12:13:22 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.084 |  |
| 2026-05-30 13:01:00 | Ellagawa (Kalu Ganga) | 7.67 | 🟢 Normal | -0.087 |  |
| 2026-05-30 12:06:14 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.090 |  |
| 2026-05-30 12:07:03 | Magura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)