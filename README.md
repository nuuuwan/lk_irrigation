# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_21:13:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,139 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 21:13:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:11:40 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-17 21:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 21:04:31 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-06-17 21:03:02 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-06-17 21:05:45 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-06-17 21:11:40 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-17 21:02:48 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-17 21:04:37 | Rathnapura (Kalu Ganga) | 3.27 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-17 21:03:29 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-17 21:03:35 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-17 21:06:04 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:07:35 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:01:14 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:04:00 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:00:31 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:03:20 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:01:38 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:13:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:07:22 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:01:51 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:02:33 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:02:39 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:04:36 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:02:56 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:07:06 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:05:01 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:02:40 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:06:06 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:01:31 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:03:26 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:03:49 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-17 21:03:36 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.021 |  |
| 2026-06-17 21:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.022 |  |
| 2026-06-17 21:01:46 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.052 |  |
| 2026-06-17 21:03:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-06-17 21:06:00 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.063 |  |
| 2026-06-17 21:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.087 |  |
| 2026-06-17 21:03:05 | Deraniyagala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.340 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)