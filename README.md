# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_00:31:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,239 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 00:31:52 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-18 00:31:46 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:16:02 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-06-18 00:12:09 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-18 00:10:27 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.143 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 00:02:02 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-06-18 00:04:20 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-06-18 00:02:13 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-17 23:03:15 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-18 00:03:29 | Peradeniya (Mahaweli Ganga) | 2.44 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-18 00:07:01 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-18 00:31:52 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-18 00:06:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-18 00:08:54 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-18 00:03:22 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-18 00:12:09 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-18 00:04:25 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-17 23:05:06 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.005 |  |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:01:38 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:03:15 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:01:45 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:02:28 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:06:28 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:03:28 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:09:06 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:07:54 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:04:00 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:06:07 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:04:54 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:02:33 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:00:52 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:04:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:31:46 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:02:13 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:04:19 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-18 00:05:17 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-06-18 00:16:02 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-06-18 00:08:40 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-06-17 21:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.022 |  |
| 2026-06-18 00:04:32 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.089 |  |
| 2026-06-18 00:10:27 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.143 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)