# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_13:33:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **186,303 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 13:33:59 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:22:04 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:17:28 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-06-22 13:17:11 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-22 13:09:15 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.073 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 13:02:19 | Ellagawa (Kalu Ganga) | 6.68 | 🟢 Normal | 6.747 | 🔺 Rising |
| 2026-06-22 13:02:34 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-06-22 13:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-06-22 13:02:59 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-06-22 13:17:28 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-06-22 13:05:47 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-06-22 13:08:43 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-06-22 13:02:42 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-06-22 13:04:09 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-22 13:09:15 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-22 13:01:33 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-22 13:06:22 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-22 13:06:17 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-22 13:07:38 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 13:03:56 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 13:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 13:06:13 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 13:06:21 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-22 13:17:11 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-22 13:03:31 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:00:47 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:01:29 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:01:11 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:06:16 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:04:06 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:03:23 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:04:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:04:21 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:33:59 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:02:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:22:04 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:05:49 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:02:28 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 13:05:47 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.009 |  |
| 2026-06-22 13:00:30 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-06-22 13:06:20 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-06-22 13:05:33 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.040 |  |
| 2026-06-22 13:04:43 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.095 |  |
| 2026-06-22 13:04:13 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.224 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)