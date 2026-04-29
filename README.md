# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_13:02:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,210 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 13:02:43 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-04-29 13:02:43 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:02:41 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.023 |  |
| 2026-04-29 13:02:38 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.010 |  |
| 2026-04-29 13:02:33 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.090 |  |
| 2026-04-29 13:02:31 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:02:29 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:02:01 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.023 |  |
| 2026-04-29 13:01:55 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-29 13:01:33 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.010 |  |
| 2026-04-29 13:01:27 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.042 |  |
| 2026-04-29 13:01:25 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:01:13 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:00:56 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-29 12:19:02 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:14:27 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-04-29 12:11:57 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 12:03:37 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-29 12:06:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-29 12:06:14 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-29 11:57:56 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-29 12:00:12 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 13:01:13 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:02:31 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:04:29 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:04:38 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:03:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:04:08 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:00:56 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:02:43 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:03:04 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:02:29 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:04:40 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:05:44 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:01:25 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:02:14 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:11:57 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 12:03:39 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-29 13:02:38 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.010 |  |
| 2026-04-29 13:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-29 13:01:33 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.010 |  |
| 2026-04-29 13:01:55 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-29 12:03:46 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.013 |  |
| 2026-04-29 12:09:40 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-04-29 12:08:00 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-04-29 12:01:50 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-04-29 13:02:43 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-04-29 12:01:18 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-04-29 12:14:27 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-04-29 12:04:27 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-04-29 13:02:41 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.023 |  |
| 2026-04-29 13:02:01 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.023 |  |
| 2026-04-29 12:03:08 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.041 |  |
| 2026-04-29 13:01:27 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.042 |  |
| 2026-04-29 13:02:33 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.090 |  |
| 2026-04-29 12:05:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)